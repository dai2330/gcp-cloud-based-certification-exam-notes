# GCP ACE 知識筆記

以 MkDocs Material 建立的 Google Cloud 課程筆記網站。每份課程 Markdown 對應一個完整網頁，Chapter 保留為頁內章節；網站可在桌面與手機閱讀，並透過 GitHub Actions 部署至 GitHub Pages。

## 專案結構

```text
.
├── docs/
│   ├── index.md
│   ├── ace/learning-path.md
│   ├── courses/ace/<course-series>/<course-slug>.md
│   └── assets/
├── templates/course-note-template.md
├── tests/test_site.py
├── mkdocs.yml
└── requirements.txt
```

`site/` 是建置產物，已由 `.gitignore` 排除，不應提交。

## 本機啟動

需要 Python 3.10 以上；GitHub Actions 使用 Python 3.13。

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m mkdocs serve
```

瀏覽 <http://127.0.0.1:8000/>。結束後按 `Ctrl+C`。

若 PowerShell 阻擋虛擬環境啟用，可不啟用環境，直接使用：

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m mkdocs serve
```

### WSL

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m mkdocs serve
```

如果專案位於 Windows 磁碟且自動重載反應較慢，可改用 `python -m mkdocs serve --dirtyreload`。

## 驗證與建置

```bash
python -m unittest discover -s tests -v
python -m mkdocs build --strict
```

嚴格模式會將未解析的連結、錯誤設定與建置警告視為失敗。成功後的靜態網站位於 `site/`。

## GitHub Pages 部署

1. 將 repository 預設分支設為 `main`。
2. 到 GitHub repository 的 **Settings → Pages**。
3. 在 **Build and deployment → Source** 選擇 **GitHub Actions**。
4. 推送 `docs/`、`mkdocs.yml` 或 workflow 的變更至 `main`。
5. 到 **Actions** 查看 `Build and deploy MkDocs to GitHub Pages`。

Workflow 會先執行測試與 `python -m mkdocs build --strict`，成功後才上傳 Pages artifact 並部署。它只使用 GitHub 自動提供的權限，不需要 Personal Access Token。

專案型 Pages 網址為：

```text
https://dai2330.github.io/gcp-cloud-based-certification-exam-notes/
```

### 自訂網域預留

需要自訂網域時，先在 **Settings → Pages → Custom domain** 完成驗證與 DNS 設定。不要只提交 `CNAME` 就假設設定已生效；暫時沒有自訂網域時不建立 `CNAME`。

## 新增下一篇課程筆記

1. 複製 `templates/course-note-template.md`。
2. 依 `docs/courses/<證照>/<課程系列>/` 建立或沿用資料夾。
3. 將檔名改為小寫 kebab-case，例如：

   ```text
   essential-google-cloud-infrastructure-core-services.md
   ```

4. 每門課程只保留一個 H1；Chapter 使用 H2，Chapter 內的區塊使用 H3。
5. 在 `mkdocs.yml` 的 `nav` 對應課程系列下加入頁面。
6. 執行完整測試與嚴格建置。

沒有內容的課程、速查表或架構圖頁面不加入導覽。

## 內容規則

- Google Cloud 服務名稱保留官方英文。
- 技術查證優先連結 Google Cloud 官方文件。
- 指令使用 `bash` code fence；Terminal Output 使用 `text` code fence。
- 只有實際執行過的內容可標為「實際執行結果」。
- 推測或示意內容必須標為「範例輸出」或「預期輸出」。
- 不提交 project credentials、service account key、access token、cookie、`.env` 或含敏感資訊的截圖與輸出。

## 常見錯誤排查

### `mkdocs` 無法找到

確認使用安裝套件的同一個 Python：

```bash
python -m pip show mkdocs-material
python -m mkdocs --version
```

### GitHub Pages 顯示 404

- 確認 Settings → Pages 的 Source 是 GitHub Actions。
- 確認 `site_url`、repository 名稱和 Pages URL 一致。
- 查看 Actions 中 build 與 deploy job 的完整 log。
- 確認 workflow 是從 `main` 觸發。

### 內部連結建置失敗

Markdown 來源連結使用相對 `.md` 路徑，不要手寫本機絕對路徑。執行 `python -m mkdocs build --strict` 取得來源檔與行號。

### Mermaid 沒有顯示

- code fence 必須是 `mermaid`。
- 查看瀏覽器 console 是否有 Mermaid 語法錯誤或資產載入錯誤；圖表由 Material for MkDocs 原生整合處理。
- 確認圖表語法沒有使用 Mermaid 不支援的節點文字。

### 手機上的表格或圖太寬

網站會提供橫向捲動。複雜 Mermaid 圖仍應拆成概觀圖與細節圖，避免在單張圖堆入過多節點。

## 敏感資料

部署不需要把 Token 或密碼寫入 repository。提交前檢查 Git 變更，若操作紀錄包含 project ID、email、IP 或其他識別資訊，先確認是否適合公開。
