import os

app_jsx_path = r"c:/Users/utkar/Desktop/Projects/document-organizer/frontend/src/App.jsx"

with open(app_jsx_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add translation keys
en_insert = """    system: "System Management",
    systemHeading: "System Management",
    systemSub: "Monitor workstation status, manage classification taxonomies, run cold backups, and configure system preferences.",
    dashboard: "Workstation Monitor\","""

hi_insert = """    system: "सिस्टम प्रबंधन",
    systemHeading: "सिस्टम प्रबंधन",
    systemSub: "कार्यस्थान की स्थिति की निगरानी करें, वर्गीकरण प्रबंधित करें, कोल्ड बैकअप चलाएं और सिस्टम प्राथमिकताएं कॉन्फ़िगर करें।",
    dashboard: "कार्यस्थान मॉनिटर\","""

content = content.replace('    dashboard: "Workstation Monitor",', en_insert)
content = content.replace('    dashboard: "कार्यस्थान मॉनिटर",', hi_insert)

# 2. Add sub-tab state hooks under function App() {
state_insert = """function App() {
  const [activeSearchSubTab, setActiveSearchSubTab] = useState("searchList");
  const [activeSystemSubTab, setActiveSystemSubTab] = useState("dashboard");"""

content = content.replace('function App() {', state_insert)

# 3. Change default landing tab to search
content = content.replace('defaultTab: "dashboard",', 'defaultTab: "search",')

# 4. Update header preferences cog button action
old_pref_btn = """          {/* Preferences Button */}
          <button
            onClick={() => setIsPrefOpen(true)}
            className="p-1.5 rounded-lg bg-slate-955 border border-slate-800 text-slate-400 hover:bg-slate-800 hover:text-indigo-400 transition-all cursor-pointer flex items-center justify-center h-7 w-7"
          >
            <i className="fa-solid fa-sliders text-[11px]"></i>
          </button>"""

new_pref_btn = """          {/* Preferences Button */}
          <button
            onClick={() => { setActiveTab("system"); setActiveSystemSubTab("preferences"); }}
            className="p-1.5 rounded-lg bg-slate-955 border border-slate-800 text-slate-400 hover:bg-slate-800 hover:text-indigo-400 transition-all cursor-pointer flex items-center justify-center h-7 w-7"
          >
            <i className="fa-solid fa-sliders text-[11px]"></i>
          </button>"""

content = content.replace(old_pref_btn, new_pref_btn)

# 5. Update SidebarAside navigation
old_sidebar = """        {/* Sidebar */}
        <aside className="w-18 bg-slate-900/90 border-r border-slate-800 p-3 flex flex-col items-center justify-between select-none">
          <div className="w-full flex flex-col items-center">
            <div className="flex items-center justify-center mb-6">
              <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-500 to-purple-600 flex items-center justify-center font-bold text-xl shadow-lg shadow-indigo-500/30 text-white">
                {appConfig.appName.charAt(0)}
              </div>
            </div>

            <nav className="space-y-3 w-full flex flex-col items-center">
              <button
                onClick={() => handleTabChange("dashboard")}
                className={`w-10 h-10 flex items-center justify-center rounded-xl transition-all ${
                  activeTab === "dashboard"
                    ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/20 font-semibold"
                    : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200"
                }`}
              >
                <i className="fa-solid fa-chart-line text-sm"></i>
              </button>
              <button
                onClick={() => handleTabChange("explorer")}
                className={`w-10 h-10 flex items-center justify-center rounded-xl transition-all ${
                  activeTab === "explorer"
                    ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/20 font-semibold"
                    : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200"
                }`}
              >
                <i className="fa-solid fa-folder-tree text-sm"></i>
              </button>
              <button
                onClick={() => handleTabChange("search")}
                className={`w-10 h-10 flex items-center justify-center rounded-xl transition-all ${
                  activeTab === "search"
                    ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/20 font-semibold"
                    : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200"
                }`}
              >
                <i className="fa-solid fa-magnifying-glass text-sm"></i>
              </button>
              <button
                onClick={() => handleTabChange("upload")}
                className={`w-10 h-10 flex items-center justify-center rounded-xl transition-all ${
                  activeTab === "upload"
                    ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/20 font-semibold"
                    : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200"
                }`}
              >
                <i className="fa-solid fa-file-import text-sm"></i>
              </button>
              <button
                onClick={() => handleTabChange("categories")}
                className={`w-10 h-10 flex items-center justify-center rounded-xl transition-all ${
                  activeTab === "categories"
                    ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/20 font-semibold"
                    : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200"
                }`}
              >
                <i className="fa-solid fa-tags text-sm"></i>
              </button>

              <button
                onClick={() => handleTabChange("backup")}
                className={`w-10 h-10 flex items-center justify-center rounded-xl transition-all ${
                  activeTab === "backup"
                    ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/20 font-semibold"
                    : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200"
                }`}
              >
                <i className="fa-solid fa-database text-sm"></i>
              </button>
            </nav>
          </div>"""

new_sidebar = """        {/* Sidebar */}
        <aside className="w-18 bg-slate-900/90 border-r border-slate-800 p-3 flex flex-col items-center justify-between select-none">
          <div className="w-full flex flex-col items-center">
            <div className="flex items-center justify-center mb-6">
              <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-500 to-purple-600 flex items-center justify-center font-bold text-xl shadow-lg shadow-indigo-500/30 text-white">
                {appConfig.appName.charAt(0)}
              </div>
            </div>

            <nav className="space-y-3 w-full flex flex-col items-center">
              <button
                onClick={() => handleTabChange("search")}
                className={`w-10 h-10 flex items-center justify-center rounded-xl transition-all ${
                  activeTab === "search"
                    ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/20 font-semibold"
                    : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200"
                }`}
              >
                <i className="fa-solid fa-magnifying-glass text-sm"></i>
              </button>
              <button
                onClick={() => handleTabChange("upload")}
                className={`w-10 h-10 flex items-center justify-center rounded-xl transition-all ${
                  activeTab === "upload"
                    ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/20 font-semibold"
                    : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200"
                }`}
              >
                <i className="fa-solid fa-file-import text-sm"></i>
              </button>
              <button
                onClick={() => handleTabChange("system")}
                className={`w-10 h-10 flex items-center justify-center rounded-xl transition-all ${
                  activeTab === "system"
                    ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/20 font-semibold"
                    : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200"
                }`}
              >
                <i className="fa-solid fa-sliders text-sm"></i>
              </button>
            </nav>
          </div>"""

content = content.replace(old_sidebar, new_sidebar)

# 6. Replace Main Content Area
# Let's extract the old main content area and replace it.
# We'll search for the block between '<main className="flex-1 p-6 overflow-y-auto bg-slate-955/60 backdrop-blur-lg">' and '</main>'
main_start = '<main className="flex-1 p-6 overflow-y-auto bg-slate-955/60 backdrop-blur-lg">'
main_end = '</main>'

start_idx = content.find(main_start)
end_idx = content.find(main_end, start_idx)

if start_idx == -1 or end_idx == -1:
    print("Failed to locate <main> tags")
    os._exit(1)

old_main_body = content[start_idx + len(main_start) : end_idx]

# Let's check: we will insert search tab, upload tab, and system tab
# But first, let's write out the system tab components (Dashboard, Categories, Backup, Preferences)
new_main_body = """
          
          {/* Ingest Tab */}
          {activeTab === "upload" && (
            <div className="max-w-2xl space-y-4 animate-fadeIn">
              <div>
                <h2 className="text-3xl font-extrabold bg-gradient-to-r from-white to-slate-400 bg-clip-text text-transparent">
                  {t("ingestHeading")}
                </h2>
                <p className="text-slate-400 mt-1">{t("ingestSub")}</p>
              </div>

              <form onSubmit={handleUploadSubmit} className="space-y-5 bg-slate-900/30 border border-slate-800/80 p-5 rounded-xl backdrop-blur-md">
                <div>
                  <label className="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">Select File</label>
                  <div className="border-2 border-dashed border-slate-800 hover:border-indigo-500/50 rounded-2xl p-5 transition-all flex flex-col items-center justify-center cursor-pointer bg-slate-955/40 relative">
                    <input
                      type="file"
                      onChange={(e) => setUploadFile(e.target.files[0])}
                      className="absolute inset-0 opacity-0 cursor-pointer"
                    />
                    <i className="fa-solid fa-cloud-arrow-up text-3xl text-indigo-400 mb-2"></i>
                    <p className="text-sm font-semibold mt-2 text-slate-355">
                      {uploadFile ? uploadFile.name : "Drag & drop files or click to browse"}
                    </p>
                    <p className="text-xs text-slate-500 mt-1">
                      {uploadFile ? `${(uploadFile.size / 1024 / 1024).toFixed(2)} MB` : "Supports PDFs, Images, Word, and Excel"}
                    </p>
                  </div>
                </div>

                <div className="grid grid-cols-2 gap-3">
                  <div>
                    <label className="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">Category</label>
                    <select
                      value={selectedCatId}
                      onChange={(e) => handleCategoryChange(e.target.value)}
                      className="w-full bg-slate-955 border border-slate-800 rounded-xl px-4 py-3.5 text-sm focus:outline-none focus:border-indigo-500 text-slate-200"
                    >
                      <option value="">Select Category</option>
                      {categories.map(c => (
                        <option key={c.id} value={c.id}>{c.name}</option>
                      ))}
                    </select>
                  </div>
                  <div>
                    <label className="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">Subcategory</label>
                    <select
                      value={subCategory}
                      onChange={(e) => setSubCategory(e.target.value)}
                      disabled={!selectedCatId}
                      className="w-full bg-slate-955 border border-slate-800 rounded-xl px-4 py-3.5 text-sm focus:outline-none focus:border-indigo-500 text-slate-200 disabled:opacity-40"
                    >
                      <option value="">Select Subcategory</option>
                      {availableSubCategories.map(s => (
                        <option key={s.id} value={s.name}>{s.name}</option>
                      ))}
                    </select>
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">Description</label>
                  <textarea
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    placeholder="Provide keywords or brief summary for search index..."
                    className="w-full bg-slate-955 border border-slate-800 rounded-xl px-4 py-3 text-sm h-24 focus:outline-none focus:border-indigo-500 resize-none text-slate-200"
                  />
                </div>

                <button
                  type="submit"
                  className="w-full py-3.5 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 rounded-xl transition-all shadow-lg shadow-indigo-600/20 flex items-center justify-center cursor-pointer text-white"
                >
                  <i className="fa-solid fa-file-shield text-base"></i>
                </button>

                {uploadStatus && (
                  <div className={`p-4 rounded-xl text-xs font-medium ${
                    uploadStatus.includes("successfully") ? "bg-emerald-500/10 text-emerald-400" : "bg-indigo-500/10 text-indigo-400"
                  }`}>
                    {uploadStatus}
                  </div>
                )}
              </form>
            </div>
          )}

          {/* Search & Explorer Tab */}
          {activeTab === "search" && (
            <div className="space-y-4 animate-fadeIn flex flex-col h-full">
              {/* Search Sub-Tabs Header */}
              <div className="flex space-x-3 pb-2 border-b border-slate-800/80 mb-2 flex-shrink-0 select-none">
                <button
                  onClick={() => setActiveSearchSubTab("searchList")}
                  className={`px-4 py-2 text-xs font-bold uppercase tracking-wider rounded-xl transition-all flex items-center space-x-2 border cursor-pointer ${
                    activeSearchSubTab === "searchList"
                      ? "bg-indigo-650/20 border-indigo-500/30 text-indigo-400 font-semibold"
                      : "border-transparent text-slate-450 hover:bg-slate-850/40 hover:text-slate-200"
                  }`}
                >
                  <i className="fa-solid fa-magnifying-glass text-xs"></i>
                  <span>Search Registry</span>
                </button>
                <button
                  onClick={() => setActiveSearchSubTab("explorer")}
                  className={`px-4 py-2 text-xs font-bold uppercase tracking-wider rounded-xl transition-all flex items-center space-x-2 border cursor-pointer ${
                    activeSearchSubTab === "explorer"
                      ? "bg-indigo-650/20 border-indigo-500/30 text-indigo-400 font-semibold"
                      : "border-transparent text-slate-450 hover:bg-slate-850/40 hover:text-slate-200"
                  }`}
                >
                  <i className="fa-solid fa-folder-tree text-xs"></i>
                  <span>Browse Workspace</span>
                </button>
              </div>

              {activeSearchSubTab === "searchList" && (
                <div className="space-y-4">
                  <div>
                    <h2 className="text-3xl font-extrabold bg-gradient-to-r from-white to-slate-400 bg-clip-text text-transparent">
                      {t("searchHeading")}
                    </h2>
                    <p className="text-slate-400 mt-1">{t("searchSub")}</p>
                  </div>

                  {/* Filters Row */}
                  <div className="grid grid-cols-1 md:grid-cols-4 gap-4 bg-slate-900/40 border border-slate-800/80 p-3 rounded-xl">
                    <input
                      type="text"
                      placeholder="Search filenames or contents..."
                      value={searchQuery}
                      onChange={(e) => setSearchQuery(e.target.value)}
                      className="w-full bg-slate-955 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-indigo-500 transition-all text-slate-200"
                    />
                    <select
                      value={filterCategory}
                      onChange={(e) => { setFilterCategory(e.target.value); setFilterSubCategory(""); }}
                      className="w-full bg-slate-955 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-indigo-500 text-slate-300"
                    >
                      <option value="">All Categories</option>
                      {categories.map(c => (
                        <option key={c.id} value={c.name}>{c.name}</option>
                      ))}
                    </select>
                    <select
                      value={filterSubCategory}
                      onChange={(e) => setFilterSubCategory(e.target.value)}
                      disabled={!filterCategory}
                      className="w-full bg-slate-955 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-indigo-500 text-slate-300 disabled:opacity-40"
                    >
                      <option value="">All Subcategories</option>
                      {filterSubCatsAvailable.map(s => (
                        <option key={s.id} value={s.name}>{s.name}</option>
                      ))}
                    </select>
                    <select
                      value={filterType}
                      onChange={(e) => setFilterType(e.target.value)}
                      className="w-full bg-slate-955 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-indigo-500 text-slate-300"
                    >
                      <option value="">All Types</option>
                      <option value="pdf">PDF Documents</option>
                      <option value="png">PNG Images</option>
                      <option value="jpg">JPEG Images</option>
                      <option value="word">Word Files</option>
                    </select>
                  </div>

                  {/* Results Grid */}
                  <div className="space-y-4">
                    {files.length > 0 ? (
                      files.map(file => (
                        <div key={file.id} className="bg-slate-900/30 border border-slate-800 hover:border-slate-700/80 p-3.5 rounded-xl flex justify-between items-center transition-all">
                          <div>
                            <h4 className="font-bold text-slate-100">{file.fileName}</h4>
                            <p className="text-xs text-slate-500 mt-1">
                              Type: {file.fileType || "unknown"} | Size: {(file.fileSize / 1024 / 1024).toFixed(2)} MB | Path: <span className="font-mono text-slate-400">{file.filePath}</span>
                            </p>
                            {file.description && (
                              <p className="text-sm text-slate-400 mt-2 italic bg-slate-950/40 px-3 py-1.5 rounded-lg border border-slate-850/50 inline-block font-sans">
                                Description: {file.description}
                              </p>
                            )}
                          </div>
                          <div className="flex items-center space-x-3">
                            <div className="text-right">
                              <span className="px-3 py-1 bg-indigo-500/10 text-indigo-400 rounded-full text-xs font-semibold uppercase">
                                {file.category}
                              </span>
                              {file.subCategory && (
                                <span className="block text-[10px] text-slate-550 mt-1 uppercase font-semibold">
                                  {file.subCategory}
                                </span>
                              )}
                            </div>
                            <button 
                              onClick={() => handleOpenLocation(file.id)}
                              className="bg-slate-850 hover:bg-slate-750 text-slate-300 p-2.5 rounded-xl transition-all cursor-pointer border border-slate-800"
                            >
                              <i className="fa-solid fa-folder-closed text-xs"></i>
                            </button>
                            <button 
                              onClick={() => handleRunFile(file.id)}
                              className="bg-indigo-600 hover:bg-indigo-550 text-white p-2.5 rounded-xl transition-all shadow-md shadow-indigo-650/10 cursor-pointer"
                            >
                              <i className="fa-solid fa-play text-[10px]"></i>
                            </button>
                          </div>
                        </div>
                      ))
                    ) : (
                      <div className="text-center py-12 text-slate-500">No matching indexed documents found.</div>
                    )}
                  </div>
                </div>
              )}

              {activeSearchSubTab === "explorer" && (
                <div className="space-y-4 animate-fadeIn h-full flex flex-col justify-between">
                  <div>
                    <h2 className="text-3xl font-extrabold bg-gradient-to-r from-white to-slate-400 bg-clip-text text-transparent">
                      {t("explorerHeading")}
                    </h2>
                    <p className="text-slate-400 mt-1">{t("explorerSub")}</p>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-5 gap-5 flex-1 items-start">
                    {/* Folder Directory Tree Panel */}
                    <div className="md:col-span-2 bg-slate-900/40 border border-slate-800 rounded-2xl p-4 min-h-[480px] shadow-xl overflow-y-auto max-h-[500px] scrollbar-thin">
                      <h3 className="text-xs font-bold uppercase tracking-wider text-slate-450 pb-3 border-b border-slate-850 mb-4 flex items-center space-x-1.5">
                        <i className="fa-solid fa-folder-tree text-indigo-400 mr-1.5"></i> <span>organized /</span>
                      </h3>

                      {Object.keys(dirTree).length > 0 ? (
                        <div className="space-y-3.5 font-sans">
                          {Object.keys(dirTree).map(type => {
                            const typePath = type;
                            const isTypeExpanded = expandedFolders[typePath];
                            return (
                              <div key={type} className="space-y-1.5">
                                <div
                                  onClick={() => toggleFolder(typePath)}
                                  className="flex items-center space-x-2 text-sm font-bold text-slate-200 hover:text-indigo-400 cursor-pointer select-none py-1 px-2 hover:bg-slate-850/40 rounded-lg transition-colors"
                                >
                                  <i className={`fa-solid ${isTypeExpanded ? "fa-folder-open text-indigo-400" : "fa-folder text-indigo-500"} mr-1 text-xs`}></i>
                                  <span>{type}</span>
                                </div>

                                {isTypeExpanded && (
                                  <div className="pl-6 space-y-1.5 border-l border-slate-850 ml-3">
                                    {Object.keys(dirTree[type]).map(year => {
                                      const yearPath = `${type}/${year}`;
                                      const isYearExpanded = expandedFolders[yearPath];
                                      return (
                                        <div key={year} className="space-y-1.5">
                                          <div
                                            onClick={() => toggleFolder(yearPath)}
                                            className="flex items-center space-x-2 text-xs font-bold text-slate-350 hover:text-indigo-400 cursor-pointer select-none py-1 px-2 hover:bg-slate-850/40 rounded-lg transition-colors"
                                          >
                                            <i className={`fa-solid ${isYearExpanded ? "fa-folder-open text-indigo-400" : "fa-folder text-indigo-550"} mr-1 text-[10px]`}></i>
                                            <span>{year}</span>
                                          </div>

                                          {isYearExpanded && (
                                            <div className="pl-6 space-y-1 border-l border-slate-850 ml-3">
                                              {Object.keys(dirTree[type][year]).map(month => {
                                                const monthPath = `${type}/${year}/${month}`;
                                                const isMonthExpanded = expandedFolders[monthPath];
                                                return (
                                                  <div key={month} className="space-y-1">
                                                    <div
                                                      onClick={() => toggleFolder(monthPath)}
                                                      className="flex items-center space-x-1.5 text-xs text-slate-400 hover:text-indigo-400 cursor-pointer select-none py-0.5 px-2 hover:bg-slate-850/40 rounded-lg transition-colors"
                                                    >
                                                      <i className={`fa-solid ${isMonthExpanded ? "fa-folder-open text-indigo-455" : "fa-folder text-indigo-600"} mr-1 text-[9px]`}></i>
                                                      <span>{month}</span>
                                                    </div>

                                                    {isMonthExpanded && (
                                                      <div className="pl-5 space-y-0.5 border-l border-slate-850 ml-2">
                                                        {dirTree[type][year][month].map(meta => (
                                                          <div
                                                            key={meta.id}
                                                            onClick={() => setSelectedFileMeta(meta)}
                                                            className={`flex items-center space-x-1.5 text-xs py-1 px-2.5 rounded-lg cursor-pointer transition-colors ${
                                                              selectedFileMeta?.id === meta.id
                                                                ? "bg-indigo-600/20 border border-indigo-500/30 text-indigo-400 font-medium"
                                                                : "text-slate-450 hover:bg-slate-850/55 hover:text-slate-300 border border-transparent"
                                                            }`}
                                                          >
                                                            <i className="fa-solid fa-file-lines text-slate-450 mr-1.5 text-[9px]"></i>
                                                            <span className="truncate max-w-[150px]">{meta.storedPath.split("/").pop()}</span>
                                                          </div>
                                                        ))}
                                                      </div>
                                                    )}
                                                  </div>
                                                );
                                              })}
                                            </div>
                                          )}
                                        </div>
                                      );
                                    })}
                                  </div>
                                )}
                              </div>
                            );
                          })}
                        </div>
                      ) : (
                        <div className="text-center py-12 text-slate-555 text-xs italic">
                          No physically organized files indexed yet.<br/>
                          Ingest files to generate disk structure.
                        </div>
                      )}
                    </div>

                    {/* File Details Panel */}
                    <div className="md:col-span-3 bg-slate-900/30 border border-slate-800/80 rounded-2xl p-4 min-h-[480px] shadow-xl flex flex-col justify-between">
                      {selectedFileMeta ? (
                        <div className="space-y-5 animate-fadeIn">
                          <div className="pb-3 border-b border-slate-800">
                            <span className="text-[10px] bg-indigo-500/10 text-indigo-400 font-bold uppercase tracking-wider px-2 py-0.5 rounded-md">
                              {t("localMetadata")}
                            </span>
                            <h4 className="text-lg font-bold text-slate-100 mt-2 break-all">
                              {selectedFileMeta.storedPath.split("/").pop()}
                            </h4>
                          </div>

                          <div className="space-y-3.5 text-xs text-slate-350">
                            <div className="bg-slate-955/40 p-3 rounded-xl border border-slate-900">
                              <span className="text-[10px] text-slate-550 block uppercase font-bold mb-1">{t("storedPath")}</span>
                              <span className="font-mono text-indigo-400 break-all">{selectedFileMeta.storedPath}</span>
                            </div>
                            <div className="bg-slate-955/40 p-3 rounded-xl border border-slate-900">
                              <span className="text-[10px] text-slate-550 block uppercase font-bold mb-1">{t("originalPath")}</span>
                              <span className="font-mono text-slate-400 break-all">{selectedFileMeta.originalPath}</span>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                              <div className="bg-slate-955/40 p-3 rounded-xl border border-slate-900">
                                <span className="text-[10px] text-slate-550 block uppercase font-bold mb-0.5">{t("fileSizing")}</span>
                                <span className="font-semibold text-slate-200">{(selectedFileMeta.fileSize / 1024 / 1024).toFixed(3)} MB</span>
                              </div>
                              <div className="bg-slate-955/40 p-3 rounded-xl border border-slate-900">
                                <span className="text-[10px] text-slate-550 block uppercase font-bold mb-0.5">{t("formatExt")}</span>
                                <span className="font-semibold uppercase text-slate-200">{selectedFileMeta.fileType}</span>
                              </div>
                            </div>
                            <div className="bg-slate-955/40 p-3 rounded-xl border border-slate-900">
                              <span className="text-[10px] text-slate-550 block uppercase font-bold mb-1">{t("dedupSig")}</span>
                              <span className="font-mono text-slate-400 break-all">{selectedFileMeta.hash}</span>
                            </div>
                          </div>

                          <div className="pt-6 border-t border-slate-850 flex justify-end space-x-3">
                            <button 
                              onClick={() => handleOpenLocation(selectedFileMeta.id)}
                              className="bg-slate-800 hover:bg-slate-700 text-slate-300 p-2.5 rounded-xl transition-colors cursor-pointer"
                            >
                              <i className="fa-solid fa-folder-closed"></i>
                            </button>
                            <button 
                              onClick={() => handleRunFile(selectedFileMeta.id)}
                              className="bg-indigo-600 hover:bg-indigo-550 text-white p-2.5 rounded-xl transition-colors shadow-lg shadow-indigo-655/10 cursor-pointer"
                            >
                              <i className="fa-solid fa-play text-[10px]"></i>
                            </button>
                          </div>
                        </div>
                      ) : (
                        <div className="flex flex-col items-center justify-center text-slate-550 flex-1 space-y-2">
                          <i className="fa-solid fa-folder-open text-slate-655 text-3xl mb-2"></i>
                          <p className="text-xs italic">Select an organized node from the directory tree to inspect workstation resource mappings.</p>
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              )}
            </div>
          )}

          {/* System Management Hub Tab */}
          {activeTab === "system" && (
            <div className="space-y-4 animate-fadeIn flex flex-col h-full">
              {/* System Hub Sub-Tabs Header */}
              <div className="flex space-x-3 pb-2 border-b border-slate-800/80 mb-2 flex-shrink-0 select-none">
                <button
                  onClick={() => setActiveSystemSubTab("dashboard")}
                  className={`px-4 py-2 text-xs font-bold uppercase tracking-wider rounded-xl transition-all flex items-center space-x-2 border cursor-pointer ${
                    activeSystemSubTab === "dashboard"
                      ? "bg-indigo-650/20 border-indigo-500/30 text-indigo-400 font-semibold"
                      : "border-transparent text-slate-450 hover:bg-slate-850/40 hover:text-slate-200"
                  }`}
                >
                  <i className="fa-solid fa-chart-line text-xs"></i>
                  <span>Status & Telemetry</span>
                </button>
                <button
                  onClick={() => setActiveSystemSubTab("categories")}
                  className={`px-4 py-2 text-xs font-bold uppercase tracking-wider rounded-xl transition-all flex items-center space-x-2 border cursor-pointer ${
                    activeSystemSubTab === "categories"
                      ? "bg-indigo-650/20 border-indigo-500/30 text-indigo-400 font-semibold"
                      : "border-transparent text-slate-450 hover:bg-slate-850/40 hover:text-slate-200"
                  }`}
                >
                  <i className="fa-solid fa-tags text-xs"></i>
                  <span>Taxonomies</span>
                </button>
                <button
                  onClick={() => setActiveSystemSubTab("backup")}
                  className={`px-4 py-2 text-xs font-bold uppercase tracking-wider rounded-xl transition-all flex items-center space-x-2 border cursor-pointer ${
                    activeSystemSubTab === "backup"
                      ? "bg-indigo-650/20 border-indigo-500/30 text-indigo-400 font-semibold"
                      : "border-transparent text-slate-450 hover:bg-slate-850/40 hover:text-slate-200"
                  }`}
                >
                  <i className="fa-solid fa-database text-xs"></i>
                  <span>Backups</span>
                </button>
                <button
                  onClick={() => setActiveSystemSubTab("preferences")}
                  className={`px-4 py-2 text-xs font-bold uppercase tracking-wider rounded-xl transition-all flex items-center space-x-2 border cursor-pointer ${
                    activeSystemSubTab === "preferences"
                      ? "bg-indigo-650/20 border-indigo-500/30 text-indigo-400 font-semibold"
                      : "border-transparent text-slate-450 hover:bg-slate-850/40 hover:text-slate-200"
                  }`}
                >
                  <i className="fa-solid fa-gear text-xs"></i>
                  <span>Preferences</span>
                </button>
              </div>

              {activeSystemSubTab === "dashboard" && (
                <div className="space-y-5 animate-fadeIn">
                  <div>
                    <h2 className="text-3xl font-extrabold tracking-tight bg-gradient-to-r from-white to-slate-400 bg-clip-text text-transparent">
                      {t("monitorHeading")}
                    </h2>
                    <p className="text-slate-400 mt-1">{t("monitorSub")}</p>
                  </div>

                  {/* Workstation Storage Sizing Cards */}
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    {/* Physical Hard Drive Size Card */}
                    <div className="bg-slate-900/50 border border-slate-800/80 p-4 rounded-2xl shadow-lg relative overflow-hidden flex flex-col justify-between hover:border-indigo-500/40 hover:shadow-indigo-950/20 transition-all duration-300">
                      <div>
                        <span className="text-xs font-bold uppercase tracking-wider text-slate-500 flex justify-between items-center">
                          <span>{t("localWorkstation")}</span>
                          <i className="fa-solid fa-hard-drive text-indigo-400 text-xs"></i>
                        </span>
                        <div className="flex items-baseline space-x-1.5 mt-2">
                          <span className="text-3xl font-black text-slate-100">{driveUsedGB}</span>
                          <span className="text-xs font-bold text-slate-500">/ {driveTotalGB} GB {t("storageUsed")}</span>
                        </div>
                      </div>
                      <div className="mt-6">
                        <div className="flex justify-between text-[10px] font-bold text-slate-500 mb-1">
                          <span>{driveFreeGB} GB {t("storageFree")}</span>
                          <span>{driveUsedPercent}% {t("storageUtilization")}</span>
                        </div>
                        <div className="w-full h-2.5 bg-slate-950 border border-slate-800/80 rounded-full overflow-hidden">
                          <div className="h-full bg-gradient-to-r from-indigo-500 to-purple-600 rounded-full" style={{ width: `${driveUsedPercent}%` }} />
                        </div>
                      </div>
                    </div>

                    {/* Local Folder Sizing Card */}
                    <div className="bg-slate-900/50 border border-slate-800/80 p-4 rounded-2xl shadow-lg flex flex-col justify-between hover:border-indigo-500/40 hover:shadow-indigo-950/20 transition-all duration-300">
                      <div>
                        <span className="text-xs font-bold uppercase tracking-wider text-slate-500 flex justify-between items-center">
                          <span>{t("storageDirSizing")}</span>
                          <i className="fa-solid fa-folder-open text-indigo-400 text-xs"></i>
                        </span>
                        <div className="grid grid-cols-2 gap-4 mt-4">
                          <div>
                            <span className="text-[10px] text-slate-500 uppercase font-extrabold block">{t("organizedFiles")}</span>
                            <span className="text-xl font-bold text-indigo-400">{localOrganizedSizeMB} MB</span>
                          </div>
                          <div>
                            <span className="text-[10px] text-slate-500 uppercase font-extrabold block">{t("tempIngests")}</span>
                            <span className="text-xl font-bold text-indigo-400">{localUploadsSizeMB} MB</span>
                          </div>
                        </div>
                      </div>
                      <div className="text-[10px] text-slate-550 border-t border-slate-850 pt-3 mt-4">
                        {t("indexingMsg")}
                      </div>
                    </div>

                    {/* Diagnostics / Engine Card */}
                    <div className="bg-slate-900/50 border border-slate-800/80 p-4 rounded-2xl shadow-lg flex flex-col justify-between hover:border-indigo-500/40 hover:shadow-indigo-950/20 transition-all duration-300">
                      <div>
                        <span className="text-xs font-bold uppercase tracking-wider text-slate-500 flex justify-between items-center">
                          <span>{t("diagnostics")}</span>
                          <i className="fa-solid fa-microchip text-indigo-400 text-xs"></i>
                        </span>
                        <div className="space-y-1.5 mt-3 text-xs">
                          <div className="flex justify-between">
                            <span className="text-slate-500">{t("dbSystem")}:</span>
                            <span className="font-semibold text-slate-355">{t("sqliteDb")}</span>
                          </div>
                          <div className="flex justify-between">
                            <span className="text-slate-500">{t("dedupCheck")}:</span>
                            <span className="font-semibold text-emerald-400">{t("dedupActive")}</span>
                          </div>
                          <div className="flex justify-between">
                            <span className="text-slate-500">{t("workstationHost")}:</span>
                            <span className="font-semibold text-slate-355">Windows (127.0.0.1)</span>
                          </div>
                          <div className="flex justify-between">
                            <span className="text-slate-500">{t("jvmRuntime")}:</span>
                            <span className="font-semibold text-slate-355">Java 17+ OpenJDK</span>
                          </div>
                        </div>
                      </div>
                      <div className="text-[10px] text-slate-550 border-t border-slate-850 pt-3 mt-2 flex justify-between">
                        <span>{t("indexSize", { count: files.length })}</span>
                        <span className="text-indigo-400 font-bold">{t("secureLoopback")}</span>
                      </div>
                    </div>
                  </div>

                  {/* Absolute Directory Paths info */}
                  {storageStats && (
                    <div className="bg-slate-900/30 border border-slate-800/80 rounded-2xl p-6 font-mono text-[10px] text-slate-450 space-y-1 bg-gradient-to-r from-slate-950/20 to-transparent">
                      <div><span className="font-bold text-slate-500">{t("prefOrganizedRoot")}:</span> {storageStats.organizedPath}</div>
                      <div><span className="font-bold text-slate-500">{t("prefIngestTmp")}:</span> {storageStats.uploadsPath}</div>
                    </div>
                  )}

                  {/* Recent Files Table */}
                  <div className="bg-slate-900/30 border border-slate-800/80 rounded-2xl p-4">
                    <h3 className="text-base font-bold mb-3 flex items-center">
                      <i className="fa-solid fa-clock-rotate-left text-indigo-400 mr-2 text-base"></i>
                      <span>{t("recentChanges")}</span>
                    </h3>
                    {files.length > 0 ? (
                      <div className="overflow-x-auto">
                        <table className="w-full text-left text-sm text-slate-350">
                          <thead className="bg-slate-900/70 text-slate-400 text-xs font-bold uppercase">
                            <tr>
                              <th className="py-2 px-3 rounded-l-xl">{t("tableName")}</th>
                              <th className="py-2 px-3">{t("tableType")}</th>
                              <th className="py-2 px-3">{t("tableSize")}</th>
                              <th className="py-2 px-3">{t("tableCategory")}</th>
                              <th className="py-2 px-3">{t("tableSubcategory")}</th>
                              <th className="py-2 px-3 rounded-r-xl">{t("tableUploadDate")}</th>
                            </tr>
                          </thead>
                          <tbody>
                            {files.slice(0, 8).map((file) => (
                              <tr key={file.id} className="border-b border-slate-800/30 hover:bg-slate-900/40 transition-colors">
                                <td className="py-2 px-3 font-semibold text-slate-200">{file.fileName}</td>
                                <td className="py-2 px-3 font-mono text-xs text-slate-400">{file.fileType || "Unknown"}</td>
                                <td className="py-2 px-3">{(file.fileSize / 1024 / 1024).toFixed(2)} MB</td>
                                <td className="py-2 px-3">
                                  <span className="px-2 py-0.5 bg-indigo-500/10 text-indigo-400 rounded-full text-xs font-medium">
                                    {file.category}
                                  </span>
                                </td>
                                <td className="py-2 px-3 text-slate-400">{file.subCategory || "General"}</td>
                                <td className="py-2 px-3 text-slate-500">
                                  {file.uploadDate ? new Date(file.uploadDate).toLocaleDateString() : "-"}
                                </td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    ) : (
                      <div className="text-center py-10 text-slate-500">{t("noIndexedDoc")}</div>
                    )}
                  </div>
                </div>
              )}

              {activeSystemSubTab === "categories" && (
                <div className="grid grid-cols-1 md:grid-cols-3 gap-5 animate-fadeIn">
                  {/* Create Category Panel */}
                  <div className="bg-slate-900/30 border border-slate-800 p-5 rounded-2xl shadow-xl flex flex-col justify-between min-h-[220px]">
                    <div>
                      <h3 className="font-bold text-slate-100 flex items-center space-x-2">
                        <i className="fa-solid fa-plus text-indigo-400"></i>
                        <span>{t("createNewCat")}</span>
                      </h3>
                      <p className="text-slate-400 text-xs mt-1">Classification tags are stored in relational index logs.</p>
                      <form onSubmit={handleCreateCategory} className="mt-4 space-y-3">
                        <input
                          type="text"
                          placeholder={t("catNamePlaceholder")}
                          value={newCatName}
                          onChange={(e) => setNewCatName(e.target.value)}
                          className="w-full bg-slate-955 border border-slate-800 rounded-xl px-4 py-2.5 text-xs focus:outline-none focus:border-indigo-500 text-slate-350"
                        />
                        <button type="submit" className="w-full py-2.5 bg-indigo-600 hover:bg-indigo-550 rounded-xl transition-all shadow-md shadow-indigo-650/15 cursor-pointer font-bold text-xs text-white">
                          {t("btnCreate")}
                        </button>
                      </form>
                    </div>
                  </div>

                  {/* Categories List registry */}
                  <div className="md:col-span-2 space-y-4">
                    <h3 className="font-bold text-slate-350 uppercase tracking-wider text-xs flex items-center space-x-2">
                      <i className="fa-solid fa-folder-closed text-indigo-400"></i>
                      <span>{t("categoryRegistry")}</span>
                    </h3>

                    {categories.length > 0 ? (
                      <div className="grid grid-cols-1 gap-4 max-h-[500px] overflow-y-auto pr-1">
                        {categories.map(cat => (
                          <div key={cat.id} className="bg-slate-900/30 border border-slate-800/80 p-4 rounded-2xl space-y-3">
                            <div className="flex justify-between items-center pb-2 border-b border-slate-850">
                              {editingCatId === cat.id ? (
                                <div className="flex items-center space-x-2">
                                  <input
                                    type="text"
                                    value={editingCatName}
                                    onChange={(e) => setEditingCatName(e.target.value)}
                                    className="bg-slate-955 border border-slate-800 rounded-lg px-2.5 py-1 text-xs focus:outline-none focus:border-indigo-500 text-slate-350"
                                  />
                                  <button onClick={() => handleUpdateCategory(cat.id)} className="bg-emerald-600 hover:bg-emerald-500 px-2 py-1 rounded text-[10px] flex items-center justify-center cursor-pointer">
                                    <i className="fa-solid fa-check text-[9px] mr-1"></i> Save
                                  </button>
                                  <button onClick={() => { setEditingCatId(null); setEditingCatName(""); }} className="bg-slate-800 hover:bg-slate-700 px-2 py-1 rounded text-[10px] flex items-center justify-center cursor-pointer">
                                    <i className="fa-solid fa-xmark text-[9px] mr-1"></i> Cancel
                                  </button>
                                </div>
                              ) : (
                                <>
                                  <span className="font-bold text-slate-100">{cat.name}</span>
                                  <div className="flex space-x-2">
                                    <button
                                      onClick={() => { setEditingCatId(cat.id); setEditingCatName(cat.name); }}
                                      className="text-xs text-slate-400 hover:text-slate-200 cursor-pointer"
                                    >
                                      <i className="fa-solid fa-pen text-[10px]"></i>
                                    </button>
                                    <button
                                      onClick={() => handleDeleteCategory(cat.id)}
                                      className="text-xs text-slate-400 hover:text-rose-455 cursor-pointer"
                                    >
                                      <i className="fa-solid fa-trash text-[10px]"></i>
                                    </button>
                                  </div>
                                </>
                              )}
                            </div>

                            {/* Subcategories */}
                            <div className="space-y-2">
                              <span className="text-[10px] font-bold text-slate-500 uppercase tracking-wider block">{t("subcategories")}</span>
                              {cat.subCategories && cat.subCategories.length > 0 ? (
                                <div className="grid grid-cols-2 gap-2">
                                  {cat.subCategories.map(sub => (
                                    <div key={sub.id} className="flex justify-between items-center bg-slate-955/40 border border-slate-900 px-2.5 py-1.5 rounded-lg group">
                                      {editingSubId === sub.id ? (
                                        <div className="flex items-center space-x-1.5">
                                          <input
                                            type="text"
                                            value={editingSubName}
                                            onChange={(e) => setEditingSubName(e.target.value)}
                                            className="bg-slate-955 border border-slate-800 rounded px-2 py-0.5 text-xs text-slate-350 focus:outline-none"
                                          />
                                          <button onClick={() => handleUpdateSubCategory(sub.id)} className="bg-emerald-600 hover:bg-emerald-500 px-2.5 py-1 rounded text-[10px] flex items-center justify-center cursor-pointer">
                                            <i className="fa-solid fa-check text-[9px] mr-1"></i> Save
                                          </button>
                                          <button onClick={() => { setEditingSubId(null); setEditingSubName(""); }} className="bg-slate-800 hover:bg-slate-700 px-2.5 py-1 rounded text-[10px] flex items-center justify-center cursor-pointer">
                                            <i className="fa-solid fa-xmark text-[9px] mr-1"></i> Cancel
                                          </button>
                                        </div>
                                      ) : (
                                        <>
                                          <span className="text-sm text-slate-350">{sub.name}</span>
                                          <div className="flex space-x-1.5 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <button
                                              onClick={() => { setEditingSubId(sub.id); setEditingSubName(sub.name); }}
                                              className="text-[10px] text-slate-400 hover:text-slate-200 cursor-pointer"
                                            >
                                              <i className="fa-solid fa-pen text-[9px]"></i>
                                            </button>
                                            <button
                                              onClick={() => handleDeleteSubCategory(sub.id)}
                                              className="text-[10px] text-slate-400 hover:text-rose-455 cursor-pointer"
                                            >
                                              <i className="fa-solid fa-trash text-[9px]"></i>
                                            </button>
                                          </div>
                                        </>
                                      )}
                                    </div>
                                  ))}
                                </div>
                              ) : (
                                <div className="text-xs text-slate-550 italic py-1">{t("noSubDef")}</div>
                              )}
                            </div>

                            {/* Quick Add Subcategory Form */}
                            <div className="mt-4">
                              <div className="flex gap-2">
                                <input
                                  type="text"
                                  placeholder={t("newSubPlaceholder")}
                                  value={newSubName[cat.id] || ""}
                                  onChange={(e) => setNewSubName({ ...newSubName, [cat.id]: e.target.value })}
                                  onKeyDown={(e) => { if (e.key === "Enter") handleCreateSubCategory(cat.id); }}
                                  className="flex-1 bg-slate-955 border border-slate-800 rounded-xl px-3 py-2 text-xs focus:outline-none focus:border-indigo-500 text-slate-355"
                                />
                                <button
                                  onClick={() => handleCreateSubCategory(cat.id)}
                                  className="bg-slate-850 hover:bg-indigo-600 text-slate-305 hover:text-white p-2.5 rounded-xl border border-slate-800 hover:border-indigo-600 transition-all cursor-pointer"
                                >
                                  <i className="fa-solid fa-plus text-[10px]"></i>
                                </button>
                              </div>
                            </div>
                          </div>
                        ))}
                      </div>
                    ) : (
                      <div className="bg-slate-900/20 border border-slate-800 rounded-2xl p-12 text-center text-slate-500">
                        <p>{t("noCatFound")}</p>
                        <p className="text-xs text-slate-600 mt-1">{t("useFormInit")}</p>
                      </div>
                    )}
                  </div>
                </div>
              )}

              {activeSystemSubTab === "backup" && (
                <div className="space-y-5 animate-fadeIn">
                  <div>
                    <h2 className="text-3xl font-extrabold bg-gradient-to-r from-white to-slate-400 bg-clip-text text-transparent">
                      {t("backupHeading")}
                    </h2>
                    <p className="text-slate-400 mt-1">{t("backupSub")}</p>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
                    {/* Control Panel & Terminal */}
                    <div className="md:col-span-2 space-y-6">
                      {/* Backup Trigger Card */}
                      <div className="bg-slate-900/40 border border-slate-800 p-4 rounded-xl shadow-xl flex justify-between items-center backdrop-blur-md hover:border-indigo-500/30 transition-all">
                        <div>
                          <h3 className="font-bold text-slate-100 text-lg">{t("coldBackup")}</h3>
                          <p className="text-slate-400 text-sm mt-1">{t("coldBackupSub")}</p>
                        </div>
                        <button
                          onClick={handleStartBackup}
                          disabled={isBackingUp}
                          className="p-3.5 bg-gradient-to-r from-emerald-600 to-indigo-650 hover:from-emerald-500 hover:to-indigo-550 disabled:from-slate-800 disabled:to-slate-800 text-white rounded-xl transition-all shadow-lg disabled:opacity-40 disabled:cursor-not-allowed cursor-pointer"
                        >
                          {isBackingUp ? (
                            <i className="fa-solid fa-spinner animate-spin"></i>
                          ) : (
                            <i className="fa-solid fa-cloud-arrow-up"></i>
                          )}
                        </button>
                      </div>

                      {/* Terminal Logging Card */}
                      <div className="bg-slate-900/30 border border-slate-800/80 p-4 rounded-xl">
                        <div className="flex justify-between items-center mb-3">
                          <span className="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center space-x-1.5">
                            <i className="fa-solid fa-terminal text-indigo-400"></i>
                            <span>{t("websocketTunnel")}</span>
                          </span>
                          <span className={`w-2 h-2 rounded-full ${isBackingUp ? "bg-emerald-500 animate-ping" : "bg-slate-650"}`} />
                        </div>
                        <div className="font-mono text-[11px] bg-slate-955 text-indigo-400 p-3 border border-slate-800 rounded-xl h-64 overflow-y-auto space-y-1.5 scrollbar-thin shadow-inner">
                          {backupLogs.map((log, index) => (
                            <div key={index} className={
                              log.startsWith("[Error]") ? "text-rose-400 font-bold" : 
                              log.startsWith("[Client]") ? "text-slate-500" :
                              log.startsWith("[Result]") ? "text-emerald-400 font-extrabold uppercase tracking-wide py-0.5" : "text-indigo-300"
                            }>
                              {log}
                            </div>
                          ))}
                          {backupLogs.length === 0 && (
                            <div className="text-slate-600 italic">Console terminal idle. Ready to start document pack.</div>
                          )}
                        </div>
                      </div>
                    </div>

                    {/* History Table Column */}
                    <div className="bg-slate-900/30 border border-slate-800/80 p-4 rounded-xl">
                      <h3 className="font-bold text-sm text-slate-355 uppercase tracking-wider mb-4 flex items-center space-x-1.5">
                        <i className="fa-solid fa-clock-rotate-left text-indigo-400"></i>
                        <span>{t("backupHistory")}</span>
                      </h3>
                      <div className="space-y-4 max-h-[460px] overflow-y-auto pr-1">
                        {backupHistory.map(record => (
                          <div key={record.id} className="bg-slate-955/40 border border-slate-850 p-3 rounded-xl space-y-2 hover:border-slate-800 transition-colors">
                            <div className="flex justify-between items-center">
                              <span className="px-2 py-0.5 bg-emerald-500/10 text-emerald-400 rounded text-[10px] font-bold tracking-wide uppercase">
                                {record.status}
                              </span>
                              <span className="text-[10px] text-slate-550 font-medium">
                                {record.timestamp ? new Date(record.timestamp).toLocaleString() : "-"}
                              </span>
                            </div>
                            <p className="text-xs text-slate-400 font-mono break-all">{record.backupPath}</p>
                          </div>
                        ))}
                        {backupHistory.length === 0 && (
                          <div className="text-center py-8 text-slate-555 text-xs italic">{t("noBackupHistory")}</div>
                        )}
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {activeSystemSubTab === "preferences" && (
                <div className="max-w-2xl bg-slate-900/30 border border-slate-800/80 p-6 rounded-2xl backdrop-blur-md animate-fadeIn space-y-6">
                  <div>
                    <h3 className="text-xl font-bold flex items-center space-x-2.5">
                      <i className="fa-solid fa-sliders text-indigo-400"></i>
                      <span>{t("prefTitle")}</span>
                    </h3>
                    <p className="text-xs text-slate-500 mt-1">Configure defaults and manage workspace directories.</p>
                  </div>

                  <div className="space-y-5">
                    {/* Startup Tab */}
                    <div>
                      <label className="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">
                        {t("prefLandingTab")}
                      </label>
                      <select
                        value={preferences.defaultTab}
                        onChange={(e) => setPreferences({ ...preferences, defaultTab: e.target.value })}
                        className="w-full bg-slate-955 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-indigo-500 text-slate-200 font-sans animate-none"
                      >
                        <option value="search">Search & Browse</option>
                        <option value="upload">Ingest Document</option>
                        <option value="system">System Management</option>
                      </select>
                    </div>

                    {/* Deduplication Strategy */}
                    <div>
                      <label className="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">
                        {t("prefDeduplication")}
                      </label>
                      <div className="flex items-center space-x-3 bg-slate-955 border border-slate-800 rounded-xl p-4">
                        <input
                          type="checkbox"
                          id="dedup"
                          checked={preferences.dedupStrategy === "sha256"}
                          onChange={(e) => setPreferences({ ...preferences, dedupStrategy: e.target.checked ? "sha256" : "none" })}
                          className="w-4 h-4 text-indigo-600 border-slate-800 rounded focus:ring-indigo-550 focus:ring-2 focus:ring-offset-slate-900 bg-slate-955"
                        />
                        <label htmlFor="dedup" className="text-sm text-slate-300 select-none cursor-pointer">
                          {t("prefEnableDedup")}
                        </label>
                      </div>
                    </div>

                    {/* Cache Statistics Section */}
                    <div className="bg-slate-955/40 border border-slate-800 rounded-xl p-4 space-y-3">
                      <h4 className="text-xs font-bold uppercase tracking-wider text-slate-450">
                        {t("cacheHeading")}
                      </h4>
                      <div className="grid grid-cols-2 gap-4">
                        <div>
                          <span className="text-[10px] text-slate-550 uppercase font-bold block">{t("cacheSizeLabel")}</span>
                          <span className="text-sm font-semibold text-slate-200">
                            {storageStats ? (storageStats.uploadsSize / 1024 / 1024).toFixed(2) : "0.00"} MB
                          </span>
                        </div>
                        <div>
                          <span className="text-[10px] text-slate-550 uppercase font-bold block">{t("cacheCountLabel")}</span>
                          <span className="text-sm font-semibold text-slate-200">
                            {storageStats && storageStats.uploadsCount !== undefined ? storageStats.uploadsCount : 0}
                          </span>
                        </div>
                      </div>
                      <button
                        type="button"
                        onClick={handleClearCache}
                        className="w-full py-2.5 bg-rose-600 hover:bg-rose-500 hover:text-white text-slate-100 rounded-xl transition-colors cursor-pointer flex items-center justify-center font-bold text-xs"
                      >
                        <i className="fa-solid fa-trash-can text-xs mr-2"></i> {t("btnClearCache")}
                      </button>
                    </div>

                    {/* Paths Settings */}
                    <div className="space-y-3">
                      <label className="block text-xs font-bold uppercase tracking-wider text-slate-400">
                        {t("prefStoragePaths")}
                      </label>
                      <div>
                        <span className="text-[10px] text-slate-550 font-bold block mb-1">{t("prefOrganizedRoot")}</span>
                        <input
                          type="text"
                          value={preferences.storageRoot}
                          onChange={(e) => setPreferences({ ...preferences, storageRoot: e.target.value })}
                          className="w-full bg-slate-955 border border-slate-800 rounded-xl px-4 py-2 text-xs font-mono focus:outline-none focus:border-indigo-500 text-slate-300"
                        />
                      </div>
                      <div>
                        <span className="text-[10px] text-slate-550 font-bold block mb-1">{t("prefIngestTmp")}</span>
                        <input
                          type="text"
                          value={preferences.ingestTmp}
                          onChange={(e) => setPreferences({ ...preferences, ingestTmp: e.target.value })}
                          className="w-full bg-slate-955 border border-slate-800 rounded-xl px-4 py-2 text-xs font-mono focus:outline-none focus:border-indigo-500 text-slate-300"
                        />
                      </div>
                    </div>

                    {/* Backup Settings */}
                    <div className="grid grid-cols-2 gap-4">
                      <div>
                        <label className="block text-xs font-bold uppercase tracking-wider text-slate-450 mb-2">
                          {t("prefAutoBackup")}
                        </label>
                        <div className="flex items-center space-x-2 h-[46px] px-3 bg-slate-955 border border-slate-800 rounded-xl">
                          <input
                            type="checkbox"
                            id="autoSync"
                            checked={preferences.autoBackup}
                            onChange={(e) => setPreferences({ ...preferences, autoBackup: e.target.checked })}
                            className="w-3.5 h-3.5 text-indigo-600 border-slate-800 rounded focus:ring-indigo-550"
                          />
                          <label htmlFor="autoSync" className="text-xs text-slate-300 select-none cursor-pointer">
                            {t("prefAutoBackup")}
                          </label>
                        </div>
                      </div>
                      <div>
                        <label className="block text-xs font-bold uppercase tracking-wider text-slate-455 mb-2">
                          {t("prefBackupInterval")}
                        </label>
                        <select
                          value={preferences.backupInterval}
                          disabled={!preferences.autoBackup}
                          onChange={(e) => setPreferences({ ...preferences, backupInterval: e.target.value })}
                          className="w-full bg-slate-955 border border-slate-800 rounded-xl px-4 py-3 text-xs focus:outline-none focus:border-indigo-500 text-slate-200 disabled:opacity-40"
                        >
                          <option value="1">Every Hour</option>
                          <option value="4">Every 4 Hours</option>
                          <option value="12">Every 12 Hours</option>
                          <option value="24">Every 24 Hours</option>
                        </select>
                      </div>
                    </div>
                  </div>

                  <div className="flex justify-end pt-4 border-t border-slate-800">
                    <button
                      onClick={() => {
                        localStorage.setItem("document_organizer_preferences", JSON.stringify(preferences));
                        addLog("info", "Saved updated workstation preferences to localStorage.");
                      }}
                      className="bg-indigo-600 hover:bg-indigo-550 text-white font-bold px-6 py-2.5 rounded-xl text-xs transition-colors shadow-lg shadow-indigo-650/20 cursor-pointer"
                    >
                      {t("prefBtnSave")}
                    </button>
                  </div>
                </div>
              )}
            </div>
          )}
"""

# Let's replace the whole main block
content = content[:start_idx + len(main_start)] + new_main_body + content[end_idx:]

# 7. Remove Preferences Modal at the bottom
# Let's see what was the preferences modal block:
# It starts at '{/* Preferences Modal */}' (line 1861)
# Let's find it.
pref_modal_start = '      {/* Preferences Modal */}'
pref_modal_end = '      {/* Help Modal */}'

p_start_idx = content.find(pref_modal_start)
p_end_idx = content.find(pref_modal_end)

if p_start_idx != -1 and p_end_idx != -1:
    # Delete preferences modal block
    content = content[:p_start_idx] + content[p_end_idx:]

# Write updated App.jsx back to disk
with open(app_jsx_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("App.jsx refactored successfully to simplify UI!")
