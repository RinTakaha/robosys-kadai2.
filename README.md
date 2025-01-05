# robosys-kadai2.
このリポジトリは,千葉工業大学未来ロボティクス学科のロボットシステム工学課題２で使用した、ROS2のパッケージです。

## 概要
usage_trackerパッケージは、PCの使用時間を追跡し、記録するためのROS2ノードです。特定のトピックを通じて使用時間を視覚化します。

## 機能
/start_time トピックで使用時間の追跡を開始。

/stop_time トピックで使用時間の追跡を停止。

## 使用方法
### 1. Usage Tracker ノードの起動
以下のコマンドでノードを起動します：
```bash
ros2 run usage_tracker usage_tracker_node
```
### 2. 使用開始・停止メッセージの送信
以下のコマンドを使って、使用時間の追跡を開始・停止できます：
#### ・使用時間の開始:
```bash
ros2 topic pub --once /start_time std_msgs/String "data: 'start'"
```
#### ・使用時間の停止
```bash
ros2 topic pub --once /stop_time std_msgs/String "data: 'stop'"
```





