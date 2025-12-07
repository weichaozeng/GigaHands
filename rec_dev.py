import os
import argparse
from mano_dev import MANO




if __name__ == "__main__":
    data_root = "/home/zvc/Project/GigaHands/dataset/hand_poses"
    save_root = "/home/zvc/Project/GigaHands/dataset/hand_poses_vert"
    

    scenes = sorted(os.listdir(data_root))
    seq_list = []
    for scene in scenes:
        scene_root = os.path.join(data_root, scene, 'params')
        if not os.path.isdir(scene_root):
            continue
        seqs = sorted(os.listdir(scene_root))
        for seq in seqs:
            seq_path = os.path.join(scene_root, seq)
            seq_list.append(seq_path)
    print(f"Total {len(seq_list)} sequences found.")

    import multiprocessing as mp





