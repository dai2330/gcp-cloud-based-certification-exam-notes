# Google Cloud Database Selection 課程頁設計

## 目標

將 `ACE_Select_a_Google_Cloud_Database_for_Your_Applications.md` 納入 ACE 筆記網站，在新的 `Google Cloud Databases` 系列下建立單一課程頁並部署至 GitHub Pages。

## 內容與路徑

- 新頁：`docs/courses/ace/google-cloud-databases/select-a-google-cloud-database-for-your-applications.md`
- 標題：`Select a Google Cloud Database for Your Applications`
- 保留全部正文、表格、命令、程式碼註解、Mermaid 與連結原順序。
- 只調整 fenced code 外標題：課名為唯一 H1；四個 Chapter 與認證重點統整為 H2；內層標題依序下移。

## 導覽與呈現

- 在 Associate Cloud Engineer 下新增 `Google Cloud Databases` 系列，排在 Cloud Run 系列後，子項名稱為 `Select a Database for Your Applications`。
- 首頁加入第七張課程卡與第七個路徑節點；ACE 學習路線加入第 7 門課。
- 沿用目前 MkDocs Material 版型、響應式版面、搜尋與 Mermaid 呈現，不新增相依套件。

## 驗收

- 測試以 UTF-8 驗證 660 行來源、唯一 H1、四個 Chapter、四張 Mermaid、程式碼內 `#` 註解及所有入口。
- 全套測試、嚴格建置、暫存差異、產物內容與敏感資訊掃描均需成功。
- GitHub Actions 部署成功後，公開課程頁及首頁皆須回傳 HTTP 200 並包含課程標題與核心章節。
