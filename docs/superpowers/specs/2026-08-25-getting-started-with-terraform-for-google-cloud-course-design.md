# Getting Started with Terraform for Google Cloud 課程頁設計

## 目標

將 `ACE_Getting_Started_with_Terraform_for_Google_Cloud.md` 納入 ACE 筆記網站，建立新的 `Getting Started with Terraform for Google Cloud` 課程系列與獨立單頁，並部署至 GitHub Pages。

## 內容與路徑

- 新頁：`docs/courses/ace/getting-started-with-terraform-for-google-cloud/getting-started-with-terraform-for-google-cloud.md`
- 標題：`Getting Started with Terraform for Google Cloud`
- 保留全部正文、表格、命令、HCL、純文字輸出與連結原順序。
- 來源已具有唯一 H1 與完整 H2/H3 階層，只移除 H1 的 ACE 筆記尾綴；fenced code 外其餘標題層級不變。

## 導覽與呈現

- 在 Associate Cloud Engineer 下新增 `Getting Started with Terraform for Google Cloud` 系列，排在 `Logging and Monitoring in Google Cloud` 後，子項標示為 `Course Notes`。
- 首頁加入第十二張課程卡與第十二個路徑節點；ACE 學習路線加入第 12 門課。
- 沿用目前 MkDocs Material 版型、響應式版面與搜尋呈現，不新增相依套件。

## 驗收

- 測試以 UTF-8 驗證 599 行來源、唯一 H1、16 個編號 H2、11 個 HCL、3 個 Bash、3 個 text 程式碼區塊及所有入口。
- 全套測試、嚴格建置、暫存差異、產物內容與敏感資訊掃描均需成功。
- GitHub Actions 部署成功後，公開課程頁及首頁皆須回傳 HTTP 200 並包含課程標題與 Terraform 核心主題。
