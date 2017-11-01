from src.api import AbstractSupportStructureDesign
from SupportStructure.teamplay_folder.teamplay_file import teamplay
import numpy as np


class TeamPlay(AbstractSupportStructureDesign):

    def support_design_model(self, TI, depth):
        costs = []
        for i in range(len(TI)):
            costs.append(teamplay(TI[i], depth[i]))
        return np.array(costs)
