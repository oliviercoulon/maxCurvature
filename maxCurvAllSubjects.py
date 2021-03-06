import computeMaxCurvature as comp

allSub=['118124', '118730', '119126', '121618', '121921', '123117', '129129', '130821', '132017', '134425', '136732', '138231', '140319', '144125', '144428', '144832', '147030', '150726', '152831', '153429', '154936', '156031', '156233', '156637', '157942', '158540', '171532', '173536', '173637', '173940', '180129', '186444', '188347', '188448', '189450', '191942', '192136', '193239', '194645', '194746', '195950', '196346', '198350', '201111', '204420', '207123', '210415', '211316', '211417', '212116', '212217', '214423', '214726', '268850', '285345', '303119', '304020', '346137', '346945', '371843', '381543', '432332', '445543', '456346', '495255', '530635', '540436', '545345', '555651', '571144', '580044', '580650', '580751', '583858', '598568', '599065', '657659', '673455', '759869', '773257', '788876', '802844', '810843', '843151', '845458', '867468', '882161', '942658', '947668', '992673']

for sub in allSub:
    print ('Processing subject ' + sub)
    print ('\tLeft')
    meshN = sub + '_Lwhite_to_dwi.gii'
    texN = sub + '_Lwhite_maxAbsCurv.gii'
    arg=['prog', meshN, texN]
    comp.main(arg)
    print ('\tRight')
    meshN = sub + '_Rwhite_to_dwi.gii'
    texN = sub + '_Rwhite_maxAbsCurv.gii'
    arg=['prog', meshN, texN]
    comp.main(arg)
    print ('\t Done')

