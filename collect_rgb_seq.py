import os
import json
import csv

res = {}
save_path = "/home/zvc/Data/GigaHands/multiview_rgb_seq_info.json"
root = "/home/zvc/Data/GigaHands/multiview_camera_video_map.csv"
rgb_root = os.path.join(root, "multiview_rgb_videos")
params_root = os.path.join(root, "hand_poses")
with open(root, mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    i = 0
    for r in reader:
        if i == 0:
            i += 1
            continue
        scene_name = r[0]
        seq_id = r[1]
        rgb_paths = r[2:]
        mano_param_path = os.path.join(params_root, scene_name, "params", f"{int(seq_id):03d}.json")
        kp_3d_path = os.path.join(params_root, scene_name, "keypoints_3d_mano_align", f"{int(seq_id):03d}.json")
        if not os.path.exists(mano_param_path) or not os.path.exists(kp_3d_path):
            print(f"Missing mano params or kp_3d for scene {scene_name} seq {seq_id}")
            continue
        for path in rgb_paths:
            video_path = os.path.join(rgb_root, path)
            if not os.path.exists(video_path):
                print(f"Video path does not exist: {video_path}")
                continue
            elif video_path in res:
                print(f"Duplicate video path found: {video_path}")
                continue
            res[video_path] = {
                "mano_param_path": mano_param_path,
                "kp_3d_path": kp_3d_path
            }
            i += 1
with open(save_path, 'w') as f:
    json.dump(res, f, indent=2)
    print(f"Processed {i} sequences. Info saved to {save_path}")

