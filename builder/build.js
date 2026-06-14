const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const rootDir = path.resolve(__dirname, '..');

// Helper to check if a command exists in the system PATH
function commandExists(cmd) {
  const checkCmd = os.platform() === 'win32' ? 'where' : 'which';
  const result = spawnSync(checkCmd, [cmd], { shell: true });
  return result.status === 0;
}

// Helper to execute a command with inherited stdio
function runCommand(command, args, cwd, env = {}) {
  console.log(`\n> Running: ${command} ${args.join(' ')} (in ${cwd})`);
  const result = spawnSync(command, args, {
    cwd,
    stdio: 'inherit',
    shell: true,
    env: { ...process.env, ...env }
  });
  if (result.status !== 0) {
    console.error(`\n[ERROR] Command failed with exit code ${result.status}`);
    process.exit(result.status || 1);
  }
}

console.log('===================================================');
console.log('       Sanchaya Cross-Platform Build Runner        ');
console.log('===================================================');
console.log(`Platform: ${os.platform()} (${os.arch()})`);
console.log(`Workspace Root: ${rootDir}`);

// 1. Verify Prerequisites
console.log('\nChecking system prerequisites...');
const prerequisites = ['node', 'npm', 'cargo'];
let missingPrereqs = 0;
for (const req of prerequisites) {
  if (commandExists(req)) {
    console.log(`  - ${req}: Available`);
  } else {
    console.warn(`  - [WARNING] ${req} was not found in your PATH. Compilation might fail.`);
    missingPrereqs++;
  }
}

// 2. Resolve Maven command
let mavenCmd = 'mvn';
if (os.platform() === 'win32') {
  if (!commandExists('mvn')) {
    const homeDir = os.homedir();
    const potentialM2Wrapper = path.join(
      homeDir,
      '.m2',
      'wrapper',
      'dists',
      'apache-maven-3.9.6-bin',
      '3311e1d4',
      'apache-maven-3.9.6',
      'bin',
      'mvn.cmd'
    );
    if (fs.existsSync(potentialM2Wrapper)) {
      mavenCmd = potentialM2Wrapper;
    } else {
      console.warn('  - mvn: Not found in PATH or standard wrapper location.');
    }
  } else {
    console.log('  - mvn: Available');
  }
} else {
  if (!commandExists('mvn')) {
    const localMvnw = path.join(rootDir, 'backend', 'mvnw');
    if (fs.existsSync(localMvnw)) {
      mavenCmd = localMvnw;
    } else {
      console.warn('  - mvn: Not found in PATH or backend wrapper directory.');
    }
  } else {
    console.log('  - mvn: Available');
  }
}

// 3. Package Backend Service
console.log('\n[1/3] Packaging Backend Service (Spring Boot Jar)...');
runCommand(mavenCmd, ['-f', path.join('backend', 'pom.xml'), 'clean', 'package', '-DskipTests'], rootDir, { MAVEN_OPTS: '-XX:+UseSerialGC -Xmx128m -XX:MaxMetaspaceSize=64m' });

// 4. Bump Frontend Build Version
console.log('\n[2/3] Bumping Version across Workspace...');
const builderDir = path.join(rootDir, 'builder');
const pythonScript = path.join(builderDir, 'increment_version.py');
if (fs.existsSync(pythonScript)) {
  runCommand('python', ['increment_version.py', 'patch'], builderDir);
} else {
  console.warn('[WARNING] increment_version.py not found in builder directory. Skipping version bump.');
}

// 4.5 Copy Help Documentation
console.log('\nCopying help documentation to frontend public directory...');
const docsHelpDir = path.join(rootDir, 'docs', 'help');
const publicHelpDir = path.join(rootDir, 'frontend', 'public', 'help');
if (fs.existsSync(docsHelpDir)) {
  if (!fs.existsSync(publicHelpDir)) {
    fs.mkdirSync(publicHelpDir, { recursive: true });
  }
  const files = fs.readdirSync(docsHelpDir);
  for (const file of files) {
    fs.copyFileSync(path.join(docsHelpDir, file), path.join(publicHelpDir, file));
  }
  console.log('Successfully copied help guides to ' + publicHelpDir);
} else {
  console.warn('[WARNING] docs/help directory not found.');
}

// 5. Build Tauri Standalone Application
console.log('\n[3/3] Compiling Frontend Client (Tauri Standalone App)...');

// Clean Rust build cache to avoid file locking issues on subsequent builds
const cargoTomlDir = path.join(frontendDir, 'src-tauri');
if (fs.existsSync(cargoTomlDir)) {
  console.log('Cleaning Rust cargo compile cache...');
  runCommand('cargo', ['clean'], cargoTomlDir);
}

// Ensure dependencies are installed in frontend
console.log('Installing frontend dependencies...');
runCommand('npm', ['install'], frontendDir);

// Build Tauri app (limiting parallel compilation threads to 1 and increasing compiler thread stack size to avoid crashes)
const extraEnv = { CARGO_BUILD_JOBS: '1', RUST_MIN_STACK: '268435456', NODE_OPTIONS: '--max-old-space-size=256' };
console.log('Building Tauri release application...');
runCommand('npm', ['run', 'tauri', 'build'], frontendDir, extraEnv);

console.log('\n===================================================');
console.log('     [SUCCESS] Production build completed!         ');
console.log('===================================================');
console.log(`Backend Jar: backend/target/sanchaya-1.0-SNAPSHOT.jar`);
console.log(`Frontend Standalone App: frontend/src-tauri/target/release/`);
console.log('===================================================\n');
process.exit(0);
