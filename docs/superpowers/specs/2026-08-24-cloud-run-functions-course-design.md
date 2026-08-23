# Cloud Run Functions 課程頁設計

## 目標

將 `ACE_Developing_Applications_with_Cloud_Run_Functions_on_Google_Cloud.md` 納入 ACE 筆記網站，在既有 `Developing Applications with Cloud Run on Google Cloud` 系列下建立 Functions 單頁，並部署至 GitHub Pages。

## 內容與路徑

- 新頁：`docs/courses/ace/developing-applications-with-cloud-run/developing-applications-with-cloud-run-functions-on-google-cloud.md`
- 標題：`Developing Applications with Cloud Run Functions on Google Cloud`
- 保留全部正文、表格、命令、程式碼註解、Mermaid 與連結原順序。
- 只調整 fenced code 外標題：課名為唯一 H1；七個 Chapter 與認證重點統整為 H2；內層標題依序下移。

## 導覽與呈現

- 在既有 Cloud Run 課程系列中，排在 Fundamentals 後，子項名稱為 `Functions on Google Cloud`。
- 首頁加入第六張課程卡與第六個路徑節點；ACE 學習路線加入第 6 門課。
- 沿用目前 MkDocs Material 版型、響應式版面、搜尋與 Mermaid 呈現，不新增相依套件。

## 驗收

- 測試以 UTF-8 驗證 933 行來源、唯一 H1、七個 Chapter、六張 Mermaid、程式碼內 `#` 註解及所有入口。
- 全套測試、嚴格建置、暫存差異、產物內容與敏感資訊掃描均需成功。
- GitHub Actions 部署成功後，公開課程頁及首頁皆須回傳 HTTP 200 並包含課程標題與連結。
