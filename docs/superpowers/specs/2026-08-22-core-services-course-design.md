# Core Services 課程頁設計

## 目標

將 `ACE_Essential_Google_Cloud_Infrastructure_Core_Services.md` 納入既有 Google Cloud ACE 筆記網站，遵循已確認的「一個課程 Markdown 對應一個網頁」與「依證照及課程系列分層」規則。

## 內容與路徑

- 新頁路徑：`docs/courses/ace/essential-google-cloud-infrastructure/essential-google-cloud-infrastructure-core-services.md`
- 網頁標題：`Essential Google Cloud Infrastructure: Core Services`
- 原始正文、表格、程式碼與來源連結必須完整保留並維持原順序。
- 只調整標題層級：課程名稱保留為唯一 H1；Chapter 與課程總結成為 H2；原 H2/H3 依序下移，避免破壞單頁目錄結構。

## 導覽

- 在 `mkdocs.yml` 的 Essential Google Cloud Infrastructure 系列下，將 Core Services 排在 Foundation 後面。
- 在首頁加入 Core Services 課程卡片，並在學習路徑頁加入第 2 門課。
- 不拆分 Chapter、不建立第二套版型，也不變更現有視覺設計。

## 驗收

- 測試必須先證明新頁尚未存在，再驗證路徑、唯一 H1、五個 Chapter、正文完整性、導覽順序與首頁／學習路徑連結。
- 全套單元測試與 `mkdocs build --strict` 必須通過。
- 推送後 GitHub Actions 必須成功，公開課程網址需回傳 HTTP 200 並含課程標題。
