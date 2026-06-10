const fs = require('fs');
const path = require('path');

// Paths
const packageJsonPath = path.join(__dirname, 'package.json');
const tauriConfPath = path.join(__dirname, 'src-tauri', 'tauri.conf.json');
const cargoTomlPath = path.join(__dirname, 'src-tauri', 'Cargo.toml');

try {
  // 1. Read package.json
  const packageJsonContent = fs.readFileSync(packageJsonPath, 'utf8');
  const packageJson = JSON.parse(packageJsonContent);
  const oldVersion = packageJson.version;
  
  // Bump patch version
  const parts = oldVersion.split('.');
  if (parts.length !== 3) {
    throw new Error(`Invalid version format in package.json: ${oldVersion}`);
  }
  const major = parseInt(parts[0], 10);
  const minor = parseInt(parts[1], 10);
  const patch = parseInt(parts[2], 10) + 1;
  const newVersion = `${major}.${minor}.${patch}`;
  
  console.log(`Bumping version: ${oldVersion} -> ${newVersion}`);
  
  // 2. Update package.json
  packageJson.version = newVersion;
  fs.writeFileSync(packageJsonPath, JSON.stringify(packageJson, null, 2) + '\n', 'utf8');
  console.log('Updated package.json');
  
  // 3. Update tauri.conf.json
  if (fs.existsSync(tauriConfPath)) {
    const tauriConfContent = fs.readFileSync(tauriConfPath, 'utf8');
    const tauriConf = JSON.parse(tauriConfContent);
    if (tauriConf.package) {
      tauriConf.package.version = newVersion;
      fs.writeFileSync(tauriConfPath, JSON.stringify(tauriConf, null, 2) + '\n', 'utf8');
      console.log('Updated tauri.conf.json');
    }
  }
  
  // 4. Update Cargo.toml
  if (fs.existsSync(cargoTomlPath)) {
    let cargoContent = fs.readFileSync(cargoTomlPath, 'utf8');
    // Replace version = "X.Y.Z" under [package]
    const packageSectionIndex = cargoContent.indexOf('[package]');
    if (packageSectionIndex !== -1) {
      // Find version = "..." after [package]
      const versionRegex = /version\s*=\s*"[^"]*"/;
      const match = cargoContent.slice(packageSectionIndex).match(versionRegex);
      if (match) {
        const oldVersionString = match[0];
        const newVersionString = `version = "${newVersion}"`;
        // Replace first occurrence after [package]
        const beforePackage = cargoContent.slice(0, packageSectionIndex);
        const afterPackage = cargoContent.slice(packageSectionIndex).replace(oldVersionString, newVersionString);
        cargoContent = beforePackage + afterPackage;
        fs.writeFileSync(cargoTomlPath, cargoContent, 'utf8');
        console.log('Updated Cargo.toml');
      }
    }
  }
  
  console.log(`Success! Version bumped to ${newVersion}`);
} catch (error) {
  console.error('Error bumping version:', error.message);
  process.exit(1);
}
