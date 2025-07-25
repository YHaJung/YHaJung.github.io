---
title: "[Setting] How to make Offline Installer of Visual Studio"
categories:
- Setting
tags:
- Visual Studio
- offline
---

# 1. Install Visual Studio Online

- [https://visualstudio.microsoft.com/ko/downloads/](https://visualstudio.microsoft.com/ko/downloads/)
- Click "Free Download"

## 2. Download Visual Studio Bootstrapper

- [https://learn.microsoft.com/en-us/visualstudio/install/create-a-network-installation-of-visual-studio?view=vs-2022#download-the-visual-studio-bootstrapper-to-create-the-layout](https://learn.microsoft.com/en-us/visualstudio/install/create-a-network-installation-of-visual-studio?view=vs-2022#download-the-visual-studio-bootstrapper-to-create-the-layout)
- Click "vs_community.exe"

## 3. Run the Bootstrapper

Open CMD and run the downloaded file with under command.
--layout set the path of the output

```
vs_community.exe --layout ./VSLayout

```

## 4. Save the layout folder and Run exe file.

- Run “vs_community.exe” to begin the offline installation.