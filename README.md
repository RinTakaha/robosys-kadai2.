# robosys-kadai2.
このリポジトリは,千葉工業大学未来ロボティクス学科のロボットシステム工学課題２で使用した、ROS2のパッケージです。

## 概要
usage_trackerパッケージは、PCの使用時間を追跡し、記録するためのROS2ノードです。特定のトピックを通じて使用時間を視覚化します。

## 機能
/start_time トピックで使用時間の追跡を開始。

/stop_time トピックで使用時間の追跡を停止。

## セットアップ手順
### 1. 必要環境
・ROS 2（Humble、Foxy、Galactic など）
・ROS 2 ワークスペースが正しく設定されていること。
### 2. リポジトリのクローン
```bash
cd ~/ros2_ws/src
git clone https://github.com/RinTakaha/robosys-kadai2..git
```
### 3.パッケージのビルド
```bash
cd ~/ros2_ws
colcon build
```
### 4.ワークスペースのセットアップ
```bash
source install/setup.bash
```
