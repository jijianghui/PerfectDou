import os 
import argparse
import torch

from perfectdou.evaluation.simulation import evaluate

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    'Dou Dizhu Evaluation')
    parser.add_argument('--landlord', type=str,
            default='perfectdou/model/douzero/douzero_ADP/landlord.ckpt')
    parser.add_argument('--landlord_up', type=str,
            default='perfectdou/model/douzero/douzero_ADP/landlord_up.ckpt')
    parser.add_argument('--landlord_down', type=str,
            default='perfectdou/model/douzero/douzero_ADP/landlord_down.ckpt')
    parser.add_argument('--eval_data', type=str,
            default='eval_data.pkl')
    parser.add_argument('--num_workers', type=int, default=5)
    parser.add_argument('--gpu_device', type=str, default='0')
    args = parser.parse_args()

    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
    os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu_device
    print("0 torch.cuda.is_available():", torch.cuda.is_available())
    evaluate(args.landlord,
             args.landlord_up,
             args.landlord_down,
             args.eval_data,
             args.num_workers)
