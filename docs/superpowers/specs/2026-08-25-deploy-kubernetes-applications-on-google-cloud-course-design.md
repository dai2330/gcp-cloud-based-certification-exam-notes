# Deploy Kubernetes Applications on Google Cloud 課程頁設計

## 目標

將 `ACE_Deploy_Kubernetes_Applications_on_Google_Cloud.md` 納入 ACE 筆記網站，建立新的 `Deploy Kubernetes Applications on Google Cloud` 課程系列與獨立單頁，並部署至 GitHub Pages。

## 內容與路徑

- 新頁：`docs/courses/ace/deploy-kubernetes-applications-on-google-cloud/deploy-kubernetes-applications-on-google-cloud.md`
- 標題：`Deploy Kubernetes Applications on Google Cloud`
- 保留全部正文、表格、命令、Dockerfile、YAML、純文字輸出、Mermaid 與連結原順序。
- 課名為唯一 H1；五個 Chapter 與認證重點統整為 H2；其餘 fenced code 外標題依序下移。

## 導覽與呈現

- 在 Associate Cloud Engineer 下新增同名系列，排在 GSP313 系列後，子項標示為 `Course Notes`。
- 首頁加入第十四張課程卡與第十四個路徑節點；ACE 學習路線加入第 14 門課。
- 沿用目前 MkDocs Material 版型、響應式版面、搜尋與 Mermaid 呈現，不新增相依套件。

## 驗收

- 測試以 UTF-8 驗證 862 行來源、唯一 H1、五個 Chapter、2 張 Mermaid、29 個 Bash、1 個 Dockerfile、2 個 YAML 與 11 個 text 區塊。
- 全套測試、嚴格建置、暫存差異、產物內容與敏感資訊掃描均需成功。
- GitHub Actions 部署成功後，公開課程頁及首頁皆須回傳 HTTP 200，並包含 Artifact Registry、GKE、Deployment、Service 與 GSP318 核心內容。
