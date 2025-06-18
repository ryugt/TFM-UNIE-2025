from transformers import pipeline

classifier = pipeline("text-classification", model="elmones/autotrain-9zdgm-8peev")
result = classifier("flujo desde IP NAT interna hacia IP privada interna usando TCP en puerto HTTP, Flow Duration es 1569455, Total Fwd Packets es 4, Total Backward Packets es 0, Total Length of Fwd Packets es 24, Total Length of Bwd Packets es 0, Fwd Packet Length Max es 6, Fwd Packet Length Mean es 6, Bwd Packet Length Max es 0, Bwd Packet Length Min es 0, Bwd Packet Length Std es 0, Flow Bytes per second es 15.29193255, Flow Packets per second es 2.548655425, Flow IAT Mean es 523151.6667, Flow IAT Std es 905560.6183, Fwd IAT Mean es 523151.6667, Fwd IAT Min es 313, Bwd IAT Mean es 0, Active Mean es 0, Idle Mean es 0, Subflow Fwd Bytes es 24, Init_Win_bytes_forward es 256")
print(result)
