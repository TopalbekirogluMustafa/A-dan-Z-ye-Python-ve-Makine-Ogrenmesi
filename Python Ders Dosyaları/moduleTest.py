# -*- coding: utf-8 -*-

#%% Module Basic
#import matematikModule
#
#matematikModule.carp(2,3)
#matematikModule.topla(2,3)

#%%  Module Renameing (Yeniden İsimlendirme)

import matematikModule as mm

mm.carp(2,3)
mm.topla(2,3)

print(mm.customer["firstName"])

#%%

from matematikModule import topla

topla(2,3)

from matematikModule import customer

print(customer["firstName"])