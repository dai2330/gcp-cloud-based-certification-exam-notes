# Build Infrastructure with Terraform on Google Cloud 課程頁設計

## 目標

將 `ACE_Build_Infrastructure_with_Terraform_on_Google_Cloud.md` 納入 ACE 筆記網站，建立 `Build Infrastructure with Terraform on Google Cloud` 獨立單頁，並部署至 GitHub Pages。

## 資訊架構決策

- 不把新課程放在清單尾端，避免 Terraform 系列被其他課程分隔。
- 不搬動既有 Getting Started 課程檔案，避免破壞已發布網址。
- 在 MkDocs 導覽新增 `Terraform on Google Cloud` 系列節點，依序收納既有 Getting Started 與新的 Build Infrastructure 課程。
- 首頁與 ACE 學習路線把新課程排在 Getting Started 後；原第 13、14 門課順延為第 14、15 門。

## 內容與路徑

- 新頁：`docs/courses/ace/build-infrastructure-with-terraform-on-google-cloud/build-infrastructure-with-terraform-on-google-cloud.md`
- 公開網址：`https://dai2330.github.io/gcp-cloud-based-certification-exam-notes/courses/ace/build-infrastructure-with-terraform-on-google-cloud/build-infrastructure-with-terraform-on-google-cloud/`
- 標題：`Build Infrastructure with Terraform on Google Cloud`
- 保留全部正文、表格、Bash、HCL、純文字輸出、Mermaid 與連結原順序。
- 課名為唯一 H1；七個 Chapter 與認證重點統整為 H2；其餘 fenced code 外標題依序下移。
- 原始 Markdown 的強制換行改用 `<br>`，避免清除行尾空白時改變顯示。

## 導覽與呈現

- 首頁新增 `ACE · TERRAFORM` 課程卡，說明 modules、import、GCS remote backend、Registry network module、firewall 與 GSP345。
- ACE 學習路線新增第 13 門，GSP313 與 Deploy Kubernetes Applications 分別改為第 14、15 門。
- 沿用目前 MkDocs Material 版型、響應式版面、搜尋與 Mermaid 呈現，不新增相依套件。

## 驗收

- 測試以 UTF-8 驗證 940 行來源、唯一 H1、七個 Chapter、認證重點統整、1 張 Mermaid、13 個 Bash、11 個 HCL 與 13 個 text 區塊。
- 驗證所有非標題來源行依序保留，且新頁可從 MkDocs 導覽、首頁與學習路線進入。
- 全套測試、嚴格建置、暫存差異、產物內容與敏感資訊掃描均需成功。
- GitHub Actions 部署成功後，公開課程頁及首頁皆須回傳 HTTP 200，並包含 Import Existing Infrastructure、Remote State、Terraform Registry、Firewall 與 GSP345 核心內容。
