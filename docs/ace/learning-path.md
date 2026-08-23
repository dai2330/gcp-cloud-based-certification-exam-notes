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

### 2. Essential Google Cloud Infrastructure: Core Services

接續 Foundation，整理 IAM、儲存與資料庫、資源管理、billing、quota，以及 Monitoring 與 Logging 的 ACE 核心操作觀念。

[開始閱讀 Core Services](../courses/ace/essential-google-cloud-infrastructure/essential-google-cloud-infrastructure-core-services.md){ .md-button .md-button--primary }

### 3. Elastic Google Cloud Infrastructure: Scaling and Automation

在 Essential 系列之後，進一步掌握 network connectivity、load balancing、MIG autoscaling、Terraform 與 managed services 選型。

[開始閱讀 Scaling and Automation](../courses/ace/elastic-google-cloud-infrastructure/elastic-google-cloud-infrastructure-scaling-and-automation.md){ .md-button .md-button--primary }

### 4. Getting Started with Google Kubernetes Engine

從 container image 與 Kubernetes 物件開始，建立 GKE 叢集模式、`kubectl` 日常操作、擴縮、更新與故障排除的基礎。

[開始閱讀 GKE](../courses/ace/google-kubernetes-engine/getting-started-with-google-kubernetes-engine.md){ .md-button .md-button--primary }

### 5. Developing Applications with Cloud Run on Google Cloud: Fundamentals

掌握 Cloud Run service、revision、container runtime contract、autoscaling、service identity、IAM，以及部署與流量管理。

[開始閱讀 Cloud Run Fundamentals](../courses/ace/developing-applications-with-cloud-run/developing-applications-with-cloud-run-fundamentals.md){ .md-button .md-button--primary }

### 6. Developing Applications with Cloud Run Functions on Google Cloud

接續 Cloud Run Fundamentals，掌握 HTTP 與事件驅動函式、Eventarc、Function identity、IAM、資料服務整合及可靠性最佳實務。

[開始閱讀 Cloud Run Functions](../courses/ace/developing-applications-with-cloud-run/developing-applications-with-cloud-run-functions-on-google-cloud.md){ .md-button .md-button--primary }

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
