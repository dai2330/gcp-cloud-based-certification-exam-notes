# Logging and Monitoring in Google Cloud 課程頁設計

## 目標

將 `ACE_Logging_and_Monitoring_in_Google_Cloud.md` 納入 ACE 筆記網站，建立新的 `Logging and Monitoring in Google Cloud` 課程系列與獨立單頁，並部署至 GitHub Pages。

## 內容與路徑

- 新頁：`docs/courses/ace/logging-and-monitoring-in-google-cloud/logging-and-monitoring-in-google-cloud.md`
- 標題：`Logging and Monitoring in Google Cloud`
- 保留全部正文、表格、命令、程式碼註解、Mermaid 與連結原順序。
- 只調整 fenced code 外標題：課名為唯一 H1；五個 Chapter 與認證重點統整為 H2；內層標題依序下移。

## 導覽與呈現

- 在 Associate Cloud Engineer 下新增 `Logging and Monitoring in Google Cloud` 系列，排在 `AI Infrastructure` 後，子項標示為 `Course Notes`。
- 首頁加入第十一張課程卡與第十一個路徑節點；ACE 學習路線加入第 11 門課。
- 沿用目前 MkDocs Material 版型、響應式版面、搜尋與 Mermaid 呈現，不新增相依套件。

## 驗收

- 測試以 UTF-8 驗證 776 行來源、唯一 H1、五個 Chapter、五張 Mermaid、六個 Bash 程式碼註解及所有入口。
- 全套測試、嚴格建置、暫存差異、產物內容與敏感資訊掃描均需成功。
- GitHub Actions 部署成功後，公開課程頁及首頁皆須回傳 HTTP 200 並包含課程標題與核心章節。
