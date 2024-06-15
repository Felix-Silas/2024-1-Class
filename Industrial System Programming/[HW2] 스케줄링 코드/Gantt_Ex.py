import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

class Gantt:
    def __init__(self, file_name):
    # CSV 파일에서 데이터 읽기
        self.df = pd.read_csv(file_name, encoding='UTF-8')
    

    def plot_gantt_chart(self):
        df = self.df
        # 각 JobType에 대해 고유한 색상을 설정
        job_colors = {job: '#{:06x}'.format(random.randint(0, 0xFFFFFF)) for job in df['JobType'].unique()}
        # Red 색상이 포함되면 다시 색상 설정
        while '#ff0000' in job_colors.values():
            job_colors = {job: '#{:06x}'.format(random.randint(0, 0xFFFFFF)) for job in df['JobType'].unique()}
        plt.figure(figsize=(12, 8))

        machine_ids = list(df['MachineId'].unique())
        machine_ids = np.sort(machine_ids)  # 기계 ID를 오름차순으로 정렬

        for machine_id in machine_ids:  # 오름차순으로 순회
            machine_df = df[df['MachineId'] == machine_id]
            for idx, row in machine_df.iterrows():
                start = row['sTime']
                end = row['cTime']
                duration = row['cTime'] - row['sTime']
                due = row['Due']
                tar = row['Tar']
                time = 0
                if tar > 0:
                    if due > start and due < end:
                        time = due
                    else:
                        time = start

                # Draw the setup part (represented by a different shade)
                if row['JobType'] == 'S':
                    plt.barh(machine_id, duration, left=start, color='black', edgecolor='black', alpha=0.7)
                # Draw the job bar
                else:
                    plt.barh(machine_id, duration, left=start, color=job_colors[row['JobType']], edgecolor='black', alpha=0.7)
                    plt.text(start + duration / 2, machine_id, f"J{row['JobId']}({row['JobType']})", va='center', ha='center', color='black')
                    # Draw the tardiness part if any
                    if tar > 0:
                        plt.barh(machine_id, tar, left=time, color='red', edgecolor='black', alpha=0.7)


        # Setting up the axes and labels
        plt.yticks(machine_ids, [f"M{mid}" for mid in machine_ids])  # 머신 ID를 그대로 표시
        plt.xlabel("Time")
        plt.ylabel("Machines")
        plt.title("Gantt Chart")
        plt.gca().invert_yaxis()  # y축을 반전시켜 역순으로 표시
        plt.grid(True)
        plt.show()

        return plt
