---
title: ACE 學習路線
description: 依現有課程內容安排的 Associate Cloud Engineer 閱讀順序
---

# ACE 學習路線

這條路線只列出目前已收錄的內容。新的課程筆記加入後，再逐步擴充導覽，不建立空白佔位頁。

## 現在可以開始的課程

### 1. Essential Google Cloud Infrastructure: Foundation

建議先掌握 Google Cloud resource hierarchy、VPC 與 subnet 的 scope，再進入 Compute Engine VM 的建立、存取、disk 與 lifecycle。

[開始閱讀 Foundation](../courses/ace/essential-google-cloud-infrastructure/essential-google-cloud-infrastructure-foundation.md){ .md-button .md-button--primary }

## 建議閱讀順序

1. **Chapter 3 — Virtual Networks**：建立 VPC、subnet、route 與 firewall rule 的資源邊界觀念。
2. **Chapter 4 — Virtual Machines**：理解 VM、machine type、disk、image 與 lifecycle。
3. **Chapter 2 — Interacting with Google Cloud**：補強 Console、Cloud Shell 與 `gcloud` context。
4. **Chapter 1 — Introduction**：回顧課程定位與 cloud engineer 的工作視角。
5. **認證重點統整**：用服務選型、resource scope 與常見陷阱做最後複習。

!!! ace "ACE 準備方式"
    閱讀概念後，應在自己的測試 project 中重做指令與 Console 操作。先檢查 active account、project、region 與 zone，再建立或刪除資源。

## 後續擴充規則

每收到一份新課程 Markdown，就放入對應的「證照／課程系列」目錄，並新增一個導覽項目。Chapter 不拆成獨立頁面。
