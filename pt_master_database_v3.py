# PT Documentation Assistant Master Database v3
# Batch 2 added: ACL Allograft, ACL Accelerated, ACL Delayed, THA Posterior, THA Anterior.

protocols = {'Neck': {'Cervical': {}},
 'Arm': {'Shoulder': {'Post-operative Bankart Repair': {'status': 'indexed', 'phases': {}},
                      'Posterior Bankart Repair': {'status': 'indexed', 'phases': {}},
                      'Rotator Cuff Repair - Large Tear': {'status': 'indexed', 'phases': {}},
                      'Rotator Cuff Repair - Small/Medium Tear': {'status': 'indexed', 'phases': {}},
                      'Lower Trapezius Tendon Transfer': {'status': 'indexed', 'phases': {}}},
         'Elbow': {'Distal Biceps Repair': {'status': 'indexed', 'phases': {}},
                   'Lateral Epicondylitis (Tennis Elbow)': {'status': 'indexed', 'phases': {}}},
         'Wrist': {}},
 'Back': {'Upper': {},
          'Middle': {},
          'Lower': {'Lumbar Fusion': {'status': 'indexed', 'phases': {}},
                    'Lumbar Discectomy': {'status': 'indexed', 'phases': {}},
                    'Lumbar Laminectomy': {'status': 'indexed', 'phases': {}},
                    'Lumbar Spinal Stenosis': {'status': 'indexed', 'phases': {}},
                    'Lumbar Disc Herniation': {'status': 'indexed', 'phases': {}},
                    'Spondylolisthesis': {'status': 'indexed', 'phases': {}}}},
 'Leg': {'Hip': {'Total Hip Arthroplasty - Posterior Approach': {'phases': {'Phase I: 0-3 Days': {'goals': ['Protect '
                                                                                                            'healing '
                                                                                                            'tissue',
                                                                                                            'Minimize '
                                                                                                            'pain and '
                                                                                                            'swelling',
                                                                                                            'Increase '
                                                                                                            'ROM',
                                                                                                            'Activate '
                                                                                                            'LE '
                                                                                                            'musculature',
                                                                                                            'Perform '
                                                                                                            'ADLs '
                                                                                                            'independently'],
                                                                                                  'precautions': ['No '
                                                                                                                  'hip '
                                                                                                                  'flexion '
                                                                                                                  'greater '
                                                                                                                  'than '
                                                                                                                  '90 '
                                                                                                                  'degrees',
                                                                                                                  'No '
                                                                                                                  'hip '
                                                                                                                  'internal '
                                                                                                                  'rotation',
                                                                                                                  'No '
                                                                                                                  'hip '
                                                                                                                  'adduction '
                                                                                                                  'past '
                                                                                                                  'neutral',
                                                                                                                  'Avoid '
                                                                                                                  'twisting '
                                                                                                                  'motions',
                                                                                                                  'Follow '
                                                                                                                  'weight-bearing '
                                                                                                                  'precautions'],
                                                                                                  'brace': ['None'],
                                                                                                  'weight_bearing': ['Per '
                                                                                                                     'surgeon '
                                                                                                                     'orders'],
                                                                                                  'rom_restrictions': ['Posterior '
                                                                                                                       'hip '
                                                                                                                       'precautions'],
                                                                                                  'manual_therapy': ['Edema '
                                                                                                                     'management',
                                                                                                                     'PROM/AAROM '
                                                                                                                     'as '
                                                                                                                     'tolerated'],
                                                                                                  'therapeutic_exercise': ['Ankle '
                                                                                                                           'pumps',
                                                                                                                           'Heel '
                                                                                                                           'slides',
                                                                                                                           'LAQ',
                                                                                                                           'Hip '
                                                                                                                           'abduction',
                                                                                                                           'Quad '
                                                                                                                           'sets',
                                                                                                                           'Hamstring '
                                                                                                                           'sets',
                                                                                                                           'Glute '
                                                                                                                           'sets',
                                                                                                                           'Heel '
                                                                                                                           'raises',
                                                                                                                           'Sit '
                                                                                                                           'to '
                                                                                                                           'stand',
                                                                                                                           'Gait '
                                                                                                                           'training',
                                                                                                                           'Transfer '
                                                                                                                           'training'],
                                                                                                  'criteria_to_progress': ['Independent '
                                                                                                                           'transfers',
                                                                                                                           'Ambulate '
                                                                                                                           '100 '
                                                                                                                           'feet',
                                                                                                                           'Pain '
                                                                                                                           'controlled',
                                                                                                                           'Independent '
                                                                                                                           'ADLs']},
                                                                            'Phase II: 1-6 Weeks': {'goals': ['Improve '
                                                                                                              'ROM',
                                                                                                              'Normalize '
                                                                                                              'gait',
                                                                                                              'Improve '
                                                                                                              'strength',
                                                                                                              'Improve '
                                                                                                              'endurance'],
                                                                                                    'precautions': ['Continue '
                                                                                                                    'hip '
                                                                                                                    'precautions '
                                                                                                                    'until '
                                                                                                                    'cleared'],
                                                                                                    'brace': ['None'],
                                                                                                    'weight_bearing': ['Progress '
                                                                                                                       'per '
                                                                                                                       'surgeon'],
                                                                                                    'rom_restrictions': ['Respect '
                                                                                                                         'posterior '
                                                                                                                         'precautions'],
                                                                                                    'manual_therapy': ['Scar '
                                                                                                                       'mobilization',
                                                                                                                       'Soft '
                                                                                                                       'tissue '
                                                                                                                       'mobilization'],
                                                                                                    'therapeutic_exercise': ['Standing '
                                                                                                                             'marches',
                                                                                                                             'Hamstring '
                                                                                                                             'curls',
                                                                                                                             '4-way '
                                                                                                                             'hip',
                                                                                                                             'Step-ups',
                                                                                                                             'Step-downs',
                                                                                                                             'SLR',
                                                                                                                             'Bridge',
                                                                                                                             'Mini '
                                                                                                                             'squats',
                                                                                                                             'Bike',
                                                                                                                             'Weight '
                                                                                                                             'shifts',
                                                                                                                             'Side '
                                                                                                                             'stepping',
                                                                                                                             'Backward '
                                                                                                                             'walking'],
                                                                                                    'criteria_to_progress': ['SLR '
                                                                                                                             'without '
                                                                                                                             'lag',
                                                                                                                             'Hip '
                                                                                                                             'flexion '
                                                                                                                             '110 '
                                                                                                                             'degrees',
                                                                                                                             'Normal '
                                                                                                                             'household '
                                                                                                                             'gait',
                                                                                                                             'SLS '
                                                                                                                             'greater '
                                                                                                                             'than '
                                                                                                                             '20 '
                                                                                                                             'sec']},
                                                                            'Phase III: 6-12 Weeks': {'goals': ['Restore '
                                                                                                                'strength',
                                                                                                                'Return '
                                                                                                                'to '
                                                                                                                'functional '
                                                                                                                'activities',
                                                                                                                'Improve '
                                                                                                                'balance'],
                                                                                                      'precautions': ['Avoid '
                                                                                                                      'high-impact '
                                                                                                                      'activity',
                                                                                                                      'Avoid '
                                                                                                                      'repetitive '
                                                                                                                      'pivoting'],
                                                                                                      'brace': ['None'],
                                                                                                      'weight_bearing': ['Full'],
                                                                                                      'rom_restrictions': ['Functional '
                                                                                                                           'ROM'],
                                                                                                      'manual_therapy': ['Soft '
                                                                                                                         'tissue '
                                                                                                                         'and '
                                                                                                                         'joint '
                                                                                                                         'mobilization '
                                                                                                                         'as '
                                                                                                                         'needed'],
                                                                                                      'therapeutic_exercise': ['Clamshells',
                                                                                                                               'Band '
                                                                                                                               'hip '
                                                                                                                               'abduction',
                                                                                                                               'Lateral '
                                                                                                                               'band '
                                                                                                                               'walks',
                                                                                                                               'Hip '
                                                                                                                               'hikes',
                                                                                                                               'Squats',
                                                                                                                               'Single-leg '
                                                                                                                               'squats',
                                                                                                                               'Split '
                                                                                                                               'squats',
                                                                                                                               'Deadlifts',
                                                                                                                               'Romanian '
                                                                                                                               'deadlifts',
                                                                                                                               'Single-leg '
                                                                                                                               'bridges',
                                                                                                                               'Balance '
                                                                                                                               'training',
                                                                                                                               'Elliptical',
                                                                                                                               'Swimming'],
                                                                                                      'criteria_to_progress': ['80% '
                                                                                                                               'strength '
                                                                                                                               'symmetry',
                                                                                                                               'Community '
                                                                                                                               'ambulation',
                                                                                                                               'Pain-free '
                                                                                                                               'ROM']},
                                                                            'Phase IV: 12-16+ Weeks': {'goals': ['Return '
                                                                                                                 'to '
                                                                                                                 'recreational '
                                                                                                                 'activity',
                                                                                                                 'Maximize '
                                                                                                                 'strength',
                                                                                                                 'Improve '
                                                                                                                 'endurance'],
                                                                                                       'precautions': ['Avoid '
                                                                                                                       'high-impact '
                                                                                                                       'activity '
                                                                                                                       'unless '
                                                                                                                       'cleared'],
                                                                                                       'brace': ['None'],
                                                                                                       'weight_bearing': ['Full'],
                                                                                                       'rom_restrictions': ['Functional '
                                                                                                                            'ROM'],
                                                                                                       'manual_therapy': ['As '
                                                                                                                          'needed'],
                                                                                                       'therapeutic_exercise': ['Weighted '
                                                                                                                                'split '
                                                                                                                                'squats',
                                                                                                                                'Hip '
                                                                                                                                'thrusts',
                                                                                                                                'Bridge '
                                                                                                                                'curls',
                                                                                                                                'Side '
                                                                                                                                'planks',
                                                                                                                                'BOSU '
                                                                                                                                'planks',
                                                                                                                                'PNF '
                                                                                                                                'diagonals',
                                                                                                                                'Advanced '
                                                                                                                                'balance',
                                                                                                                                'Return-to-run '
                                                                                                                                'progression '
                                                                                                                                'if '
                                                                                                                                'cleared'],
                                                                                                       'criteria_to_progress': ['95% '
                                                                                                                                'strength '
                                                                                                                                'symmetry',
                                                                                                                                'Return '
                                                                                                                                'to '
                                                                                                                                'work',
                                                                                                                                'Surgeon '
                                                                                                                                'clearance']}}},
                 'Total Hip Arthroplasty - Anterior Approach': {'phases': {'Phase I: 0-3 Days': {'goals': ['Protect '
                                                                                                           'healing '
                                                                                                           'tissue',
                                                                                                           'Minimize '
                                                                                                           'pain and '
                                                                                                           'swelling',
                                                                                                           'Activate '
                                                                                                           'LE '
                                                                                                           'musculature',
                                                                                                           'Perform '
                                                                                                           'ADLs '
                                                                                                           'independently'],
                                                                                                 'precautions': ['No '
                                                                                                                 'hip '
                                                                                                                 'extension '
                                                                                                                 'beyond '
                                                                                                                 'neutral',
                                                                                                                 'No '
                                                                                                                 'hip '
                                                                                                                 'ER '
                                                                                                                 'beyond '
                                                                                                                 'neutral',
                                                                                                                 'No '
                                                                                                                 'combined '
                                                                                                                 'extension '
                                                                                                                 'and '
                                                                                                                 'ER',
                                                                                                                 'Maintain '
                                                                                                                 'hip '
                                                                                                                 'flexion '
                                                                                                                 'at '
                                                                                                                 'least '
                                                                                                                 '30 '
                                                                                                                 'degrees '
                                                                                                                 'when '
                                                                                                                 'supine '
                                                                                                                 'if '
                                                                                                                 'directed',
                                                                                                                 'No '
                                                                                                                 'early '
                                                                                                                 'SLR',
                                                                                                                 'No '
                                                                                                                 'early '
                                                                                                                 'heel '
                                                                                                                 'slides '
                                                                                                                 'if '
                                                                                                                 'restricted'],
                                                                                                 'brace': ['None'],
                                                                                                 'weight_bearing': ['Per '
                                                                                                                    'surgeon '
                                                                                                                    'orders'],
                                                                                                 'rom_restrictions': ['Anterior '
                                                                                                                      'hip '
                                                                                                                      'precautions'],
                                                                                                 'manual_therapy': ['Edema '
                                                                                                                    'management',
                                                                                                                    'PROM/AAROM '
                                                                                                                    'as '
                                                                                                                    'tolerated'],
                                                                                                 'therapeutic_exercise': ['Ankle '
                                                                                                                          'pumps',
                                                                                                                          'LAQ',
                                                                                                                          'Hip '
                                                                                                                          'abduction '
                                                                                                                          'if '
                                                                                                                          'allowed',
                                                                                                                          'Quad '
                                                                                                                          'sets',
                                                                                                                          'Hamstring '
                                                                                                                          'sets',
                                                                                                                          'Glute '
                                                                                                                          'sets',
                                                                                                                          'Sit '
                                                                                                                          'to '
                                                                                                                          'stand',
                                                                                                                          'Gait '
                                                                                                                          'training',
                                                                                                                          'Transfer '
                                                                                                                          'training'],
                                                                                                 'criteria_to_progress': ['Independent '
                                                                                                                          'transfers',
                                                                                                                          'Ambulate '
                                                                                                                          '100 '
                                                                                                                          'feet',
                                                                                                                          'Pain '
                                                                                                                          'controlled',
                                                                                                                          'Independent '
                                                                                                                          'ADLs']},
                                                                           'Phase II: 1-6 Weeks': {'goals': ['Improve '
                                                                                                             'ROM',
                                                                                                             'Normalize '
                                                                                                             'gait',
                                                                                                             'Improve '
                                                                                                             'strength',
                                                                                                             'Improve '
                                                                                                             'endurance'],
                                                                                                   'precautions': ['Continue '
                                                                                                                   'anterior '
                                                                                                                   'precautions '
                                                                                                                   'until '
                                                                                                                   'cleared',
                                                                                                                   'Avoid '
                                                                                                                   'combined '
                                                                                                                   'hip '
                                                                                                                   'extension '
                                                                                                                   'and '
                                                                                                                   'external '
                                                                                                                   'rotation'],
                                                                                                   'brace': ['None'],
                                                                                                   'weight_bearing': ['Progress '
                                                                                                                      'per '
                                                                                                                      'surgeon'],
                                                                                                   'rom_restrictions': ['Respect '
                                                                                                                        'anterior '
                                                                                                                        'precautions'],
                                                                                                   'manual_therapy': ['Scar '
                                                                                                                      'mobilization',
                                                                                                                      'Soft '
                                                                                                                      'tissue '
                                                                                                                      'mobilization'],
                                                                                                   'therapeutic_exercise': ['Standing '
                                                                                                                            'marches '
                                                                                                                            'within '
                                                                                                                            'precautions',
                                                                                                                            'Hamstring '
                                                                                                                            'curls',
                                                                                                                            '4-way '
                                                                                                                            'hip '
                                                                                                                            'respecting '
                                                                                                                            'precautions',
                                                                                                                            'Step-ups',
                                                                                                                            'Step-downs',
                                                                                                                            'Bridge '
                                                                                                                            'if '
                                                                                                                            'allowed',
                                                                                                                            'Mini '
                                                                                                                            'squats',
                                                                                                                            'Bike',
                                                                                                                            'Weight '
                                                                                                                            'shifts',
                                                                                                                            'Side '
                                                                                                                            'stepping',
                                                                                                                            'Backward '
                                                                                                                            'walking '
                                                                                                                            'when '
                                                                                                                            'appropriate'],
                                                                                                   'criteria_to_progress': ['Normal '
                                                                                                                            'household '
                                                                                                                            'gait',
                                                                                                                            'SLS '
                                                                                                                            'greater '
                                                                                                                            'than '
                                                                                                                            '20 '
                                                                                                                            'sec',
                                                                                                                            'Minimal '
                                                                                                                            'pain']},
                                                                           'Phase III: 6-12 Weeks': {'goals': ['Restore '
                                                                                                               'strength',
                                                                                                               'Return '
                                                                                                               'to '
                                                                                                               'functional '
                                                                                                               'activities',
                                                                                                               'Improve '
                                                                                                               'balance'],
                                                                                                     'precautions': ['Avoid '
                                                                                                                     'high-impact '
                                                                                                                     'activity',
                                                                                                                     'Avoid '
                                                                                                                     'repetitive '
                                                                                                                     'pivoting'],
                                                                                                     'brace': ['None'],
                                                                                                     'weight_bearing': ['Full'],
                                                                                                     'rom_restrictions': ['Per '
                                                                                                                          'surgeon'],
                                                                                                     'manual_therapy': ['As '
                                                                                                                        'needed'],
                                                                                                     'therapeutic_exercise': ['Clamshells',
                                                                                                                              'Band '
                                                                                                                              'hip '
                                                                                                                              'abduction',
                                                                                                                              'Lateral '
                                                                                                                              'band '
                                                                                                                              'walks',
                                                                                                                              'Hip '
                                                                                                                              'hikes',
                                                                                                                              'Squats',
                                                                                                                              'Split '
                                                                                                                              'squats',
                                                                                                                              'Single-leg '
                                                                                                                              'bridges',
                                                                                                                              'Balance '
                                                                                                                              'training',
                                                                                                                              'Elliptical',
                                                                                                                              'Swimming'],
                                                                                                     'criteria_to_progress': ['80% '
                                                                                                                              'strength '
                                                                                                                              'symmetry',
                                                                                                                              'Community '
                                                                                                                              'ambulation',
                                                                                                                              'Pain-free '
                                                                                                                              'functional '
                                                                                                                              'ROM']},
                                                                           'Phase IV: 12-16+ Weeks': {'goals': ['Return '
                                                                                                                'to '
                                                                                                                'recreational '
                                                                                                                'activity',
                                                                                                                'Maximize '
                                                                                                                'strength',
                                                                                                                'Improve '
                                                                                                                'endurance'],
                                                                                                      'precautions': ['Avoid '
                                                                                                                      'high-impact '
                                                                                                                      'activity '
                                                                                                                      'unless '
                                                                                                                      'cleared'],
                                                                                                      'brace': ['None'],
                                                                                                      'weight_bearing': ['Full'],
                                                                                                      'rom_restrictions': ['Functional '
                                                                                                                           'ROM'],
                                                                                                      'manual_therapy': ['As '
                                                                                                                         'needed'],
                                                                                                      'therapeutic_exercise': ['Weighted '
                                                                                                                               'split '
                                                                                                                               'squats',
                                                                                                                               'Hip '
                                                                                                                               'thrusts',
                                                                                                                               'Bridge '
                                                                                                                               'curls',
                                                                                                                               'Side '
                                                                                                                               'planks',
                                                                                                                               'BOSU '
                                                                                                                               'planks',
                                                                                                                               'PNF '
                                                                                                                               'diagonals',
                                                                                                                               'Advanced '
                                                                                                                               'balance',
                                                                                                                               'Return-to-run '
                                                                                                                               'progression '
                                                                                                                               'if '
                                                                                                                               'cleared'],
                                                                                                      'criteria_to_progress': ['95% '
                                                                                                                               'strength '
                                                                                                                               'symmetry',
                                                                                                                               'Return '
                                                                                                                               'to '
                                                                                                                               'work',
                                                                                                                               'Surgeon '
                                                                                                                               'clearance']}}}},
         'Knee': {'ACL Reconstruction - Patellar Tendon Autograft': {'status': 'indexed', 'phases': {}},
                  'ACL Reconstruction - Hamstring Tendon Autograft': {'phases': {'Phase I: 0-4 weeks': {'goals': ['Protect '
                                                                                                                  'graft '
                                                                                                                  'and '
                                                                                                                  'fixation',
                                                                                                                  'Control '
                                                                                                                  'inflammation '
                                                                                                                  'and '
                                                                                                                  'swelling',
                                                                                                                  'Restore '
                                                                                                                  'full '
                                                                                                                  'extension',
                                                                                                                  'Restore '
                                                                                                                  'gait',
                                                                                                                  'Protect '
                                                                                                                  'hamstring '
                                                                                                                  'donor '
                                                                                                                  'site'],
                                                                                                        'precautions': ['Avoid '
                                                                                                                        'hyperextension '
                                                                                                                        'greater '
                                                                                                                        'than '
                                                                                                                        '10 '
                                                                                                                        'degrees',
                                                                                                                        'Flexion '
                                                                                                                        'limited '
                                                                                                                        'to '
                                                                                                                        '90 '
                                                                                                                        'degrees',
                                                                                                                        'Delay '
                                                                                                                        'hamstring '
                                                                                                                        'strengthening',
                                                                                                                        'Protect '
                                                                                                                        'graft '
                                                                                                                        'fixation'],
                                                                                                        'brace': ['Week '
                                                                                                                  '0-1: '
                                                                                                                  'locked '
                                                                                                                  'in '
                                                                                                                  'extension',
                                                                                                                  'Weeks '
                                                                                                                  '1-3: '
                                                                                                                  'unlock '
                                                                                                                  'to '
                                                                                                                  'less '
                                                                                                                  'than '
                                                                                                                  '90 '
                                                                                                                  'degrees '
                                                                                                                  'as '
                                                                                                                  'quad '
                                                                                                                  'control '
                                                                                                                  'allows',
                                                                                                                  'Weeks '
                                                                                                                  '3-4: '
                                                                                                                  'wean '
                                                                                                                  'from '
                                                                                                                  'brace'],
                                                                                                        'weight_bearing': ['Week '
                                                                                                                           '0-1: '
                                                                                                                           'PWB '
                                                                                                                           'with '
                                                                                                                           'two '
                                                                                                                           'crutches',
                                                                                                                           'Weeks '
                                                                                                                           '1-4: '
                                                                                                                           'progress '
                                                                                                                           'to '
                                                                                                                           'FWB '
                                                                                                                           'with '
                                                                                                                           'normalized '
                                                                                                                           'gait'],
                                                                                                        'rom_restrictions': ['Flexion '
                                                                                                                             'limited '
                                                                                                                             'to '
                                                                                                                             '90 '
                                                                                                                             'degrees',
                                                                                                                             'Full '
                                                                                                                             'extension '
                                                                                                                             'emphasized'],
                                                                                                        'manual_therapy': ['Patellar '
                                                                                                                           'mobilization',
                                                                                                                           'Edema '
                                                                                                                           'management',
                                                                                                                           'Scar '
                                                                                                                           'mobilization'],
                                                                                                        'therapeutic_exercise': ['Heel '
                                                                                                                                 'slides',
                                                                                                                                 'Quad '
                                                                                                                                 'sets',
                                                                                                                                 'NMES '
                                                                                                                                 'if '
                                                                                                                                 'indicated',
                                                                                                                                 'Gastroc/Soleus '
                                                                                                                                 'stretching',
                                                                                                                                 'Gentle '
                                                                                                                                 'hamstring '
                                                                                                                                 'stretching '
                                                                                                                                 'at '
                                                                                                                                 'week '
                                                                                                                                 '1',
                                                                                                                                 'SLR '
                                                                                                                                 'all '
                                                                                                                                 'planes',
                                                                                                                                 'Quadriceps '
                                                                                                                                 'isometrics',
                                                                                                                                 'Aquatic '
                                                                                                                                 'therapy '
                                                                                                                                 'after '
                                                                                                                                 'suture '
                                                                                                                                 'removal'],
                                                                                                        'criteria_to_progress': ['Full '
                                                                                                                                 'extension',
                                                                                                                                 '90 '
                                                                                                                                 'degrees '
                                                                                                                                 'flexion',
                                                                                                                                 'Good '
                                                                                                                                 'quad '
                                                                                                                                 'set',
                                                                                                                                 'SLR '
                                                                                                                                 'without '
                                                                                                                                 'lag',
                                                                                                                                 'Minimal '
                                                                                                                                 'swelling',
                                                                                                                                 'Normal '
                                                                                                                                 'gait']},
                                                                                 'Phase II: 4-10 weeks': {'goals': ['Restore '
                                                                                                                    'normal '
                                                                                                                    'gait',
                                                                                                                    'Progress '
                                                                                                                    'toward '
                                                                                                                    'full '
                                                                                                                    'ROM',
                                                                                                                    'Increase '
                                                                                                                    'LE '
                                                                                                                    'strength',
                                                                                                                    'Improve '
                                                                                                                    'proprioception'],
                                                                                                          'precautions': ['Avoid '
                                                                                                                          'aggressive '
                                                                                                                          'hamstring '
                                                                                                                          'strengthening',
                                                                                                                          'Protect '
                                                                                                                          'graft '
                                                                                                                          'during '
                                                                                                                          'revascularization'],
                                                                                                          'brace': ['Continue '
                                                                                                                    'weaning '
                                                                                                                    'if '
                                                                                                                    'needed'],
                                                                                                          'weight_bearing': ['Full'],
                                                                                                          'rom_restrictions': ['Progress '
                                                                                                                               'toward '
                                                                                                                               'full '
                                                                                                                               'ROM'],
                                                                                                          'manual_therapy': ['Patellar '
                                                                                                                             'mobility',
                                                                                                                             'Soft '
                                                                                                                             'tissue '
                                                                                                                             'mobility'],
                                                                                                          'therapeutic_exercise': ['Wall '
                                                                                                                                   'sits',
                                                                                                                                   'Step-ups',
                                                                                                                                   'Mini '
                                                                                                                                   'squats',
                                                                                                                                   'Leg '
                                                                                                                                   'press '
                                                                                                                                   '90-30',
                                                                                                                                   'Progressive '
                                                                                                                                   'hip '
                                                                                                                                   'strengthening',
                                                                                                                                   'Progressive '
                                                                                                                                   'calf '
                                                                                                                                   'strengthening',
                                                                                                                                   'Hamstring '
                                                                                                                                   'strengthening '
                                                                                                                                   'begins '
                                                                                                                                   'around '
                                                                                                                                   'week '
                                                                                                                                   '12',
                                                                                                                                   'Stairmaster',
                                                                                                                                   'Elliptical',
                                                                                                                                   'Stationary '
                                                                                                                                   'bike',
                                                                                                                                   'Single-leg '
                                                                                                                                   'balance',
                                                                                                                                   'Balance '
                                                                                                                                   'beam',
                                                                                                                                   'Mini-tramp '
                                                                                                                                   'balance'],
                                                                                                          'criteria_to_progress': ['120 '
                                                                                                                                   'degrees '
                                                                                                                                   'flexion',
                                                                                                                                   'Minimal '
                                                                                                                                   'swelling',
                                                                                                                                   'Adequate '
                                                                                                                                   'strength '
                                                                                                                                   'for '
                                                                                                                                   'running']},
                                                                                 'Phase III: 10-16 weeks': {'goals': ['Restore '
                                                                                                                      'full '
                                                                                                                      'ROM',
                                                                                                                      'Improve '
                                                                                                                      'strength '
                                                                                                                      'and '
                                                                                                                      'endurance',
                                                                                                                      'Normalize '
                                                                                                                      'running '
                                                                                                                      'mechanics',
                                                                                                                      'Prepare '
                                                                                                                      'for '
                                                                                                                      'sport'],
                                                                                                            'precautions': ['Gradually '
                                                                                                                            'increase '
                                                                                                                            'hamstring '
                                                                                                                            'resistance',
                                                                                                                            'Avoid '
                                                                                                                            'graft '
                                                                                                                            'overload'],
                                                                                                            'brace': ['None'],
                                                                                                            'weight_bearing': ['Full'],
                                                                                                            'rom_restrictions': ['Full '
                                                                                                                                 'ROM'],
                                                                                                            'manual_therapy': ['As '
                                                                                                                               'needed'],
                                                                                                            'therapeutic_exercise': ['Open-chain '
                                                                                                                                     'knee '
                                                                                                                                     'extension '
                                                                                                                                     '90-30',
                                                                                                                                     'Progressive '
                                                                                                                                     'hamstring '
                                                                                                                                     'strengthening',
                                                                                                                                     'Running '
                                                                                                                                     'progression '
                                                                                                                                     'at '
                                                                                                                                     'approximately '
                                                                                                                                     '16 '
                                                                                                                                     'weeks',
                                                                                                                                     'Swimming',
                                                                                                                                     'Hip '
                                                                                                                                     'strengthening',
                                                                                                                                     'Quadriceps '
                                                                                                                                     'strengthening',
                                                                                                                                     'Hamstring '
                                                                                                                                     'strengthening',
                                                                                                                                     'Calf '
                                                                                                                                     'strengthening',
                                                                                                                                     'Bike',
                                                                                                                                     'Elliptical',
                                                                                                                                     'Advanced '
                                                                                                                                     'balance '
                                                                                                                                     'training'],
                                                                                                            'criteria_to_progress': ['Full '
                                                                                                                                     'pain-free '
                                                                                                                                     'ROM',
                                                                                                                                     '70 '
                                                                                                                                     'percent '
                                                                                                                                     'strength '
                                                                                                                                     'of '
                                                                                                                                     'uninvolved '
                                                                                                                                     'leg',
                                                                                                                                     'Normal '
                                                                                                                                     'running '
                                                                                                                                     'gait',
                                                                                                                                     'No '
                                                                                                                                     'significant '
                                                                                                                                     'swelling']},
                                                                                 'Phase IV: 4-6 months': {'goals': ['Initiate '
                                                                                                                    'agility',
                                                                                                                    'Restore '
                                                                                                                    'power',
                                                                                                                    'Return '
                                                                                                                    'to '
                                                                                                                    'sport '
                                                                                                                    'preparation'],
                                                                                                          'precautions': ['Monitor '
                                                                                                                          'donor '
                                                                                                                          'site '
                                                                                                                          'symptoms'],
                                                                                                          'brace': ['None'],
                                                                                                          'weight_bearing': ['Full'],
                                                                                                          'rom_restrictions': ['None'],
                                                                                                          'manual_therapy': ['As '
                                                                                                                             'needed'],
                                                                                                          'therapeutic_exercise': ['Plyometrics',
                                                                                                                                   'Side '
                                                                                                                                   'shuffles',
                                                                                                                                   'Crossovers',
                                                                                                                                   'Figure-8 '
                                                                                                                                   'running',
                                                                                                                                   'Shuttle '
                                                                                                                                   'runs',
                                                                                                                                   'Single-leg '
                                                                                                                                   'jumping',
                                                                                                                                   'Double-leg '
                                                                                                                                   'jumping',
                                                                                                                                   'Cutting '
                                                                                                                                   'drills',
                                                                                                                                   'Acceleration '
                                                                                                                                   'drills',
                                                                                                                                   'Deceleration '
                                                                                                                                   'drills',
                                                                                                                                   'Sprint '
                                                                                                                                   'progression',
                                                                                                                                   'Agility '
                                                                                                                                   'ladder'],
                                                                                                          'criteria_to_progress': ['85 '
                                                                                                                                   'percent '
                                                                                                                                   'hop '
                                                                                                                                   'testing',
                                                                                                                                   '85 '
                                                                                                                                   'percent '
                                                                                                                                   'quadriceps '
                                                                                                                                   'strength',
                                                                                                                                   '85 '
                                                                                                                                   'percent '
                                                                                                                                   'hamstring '
                                                                                                                                   'strength']},
                                                                                 'Phase V: 6+ months': {'goals': ['Return '
                                                                                                                  'to '
                                                                                                                  'sport',
                                                                                                                  'Maintain '
                                                                                                                  'strength',
                                                                                                                  'Maintain '
                                                                                                                  'endurance'],
                                                                                                        'precautions': ['Follow '
                                                                                                                        'surgeon '
                                                                                                                        'clearance'],
                                                                                                        'brace': ['Functional '
                                                                                                                  'brace '
                                                                                                                  'only '
                                                                                                                  'if '
                                                                                                                  'prescribed'],
                                                                                                        'weight_bearing': ['Full'],
                                                                                                        'rom_restrictions': ['None'],
                                                                                                        'manual_therapy': ['As '
                                                                                                                           'needed'],
                                                                                                        'therapeutic_exercise': ['Sport-specific '
                                                                                                                                 'drills',
                                                                                                                                 'Advanced '
                                                                                                                                 'agility',
                                                                                                                                 'Maintenance '
                                                                                                                                 'strengthening',
                                                                                                                                 'Return-to-sport '
                                                                                                                                 'progression'],
                                                                                                        'criteria_to_progress': ['Physician '
                                                                                                                                 'clearance',
                                                                                                                                 'Functional '
                                                                                                                                 'testing '
                                                                                                                                 'passed']}}},
                  'ACL Reconstruction - Allograft': {'phases': {'Phase I: 0-6 weeks': {'goals': ['Protect graft '
                                                                                                 'fixation',
                                                                                                 'Control inflammation',
                                                                                                 'Restore full '
                                                                                                 'extension',
                                                                                                 'Restore flexion to '
                                                                                                 '90 degrees',
                                                                                                 'Normalize gait '
                                                                                                 'mechanics'],
                                                                                       'precautions': ['Allograft '
                                                                                                       'healing is '
                                                                                                       'slower than '
                                                                                                       'autograft',
                                                                                                       'Protect graft '
                                                                                                       'fixation',
                                                                                                       'Avoid '
                                                                                                       'excessive '
                                                                                                       'loading'],
                                                                                       'brace': ['Brace locked in '
                                                                                                 'extension first week',
                                                                                                 'Brace used for '
                                                                                                 'ambulation for 6 '
                                                                                                 'weeks'],
                                                                                       'weight_bearing': ['Weeks 0-2: '
                                                                                                          'Partial '
                                                                                                          'weight '
                                                                                                          'bearing',
                                                                                                          'Weeks 2-4: '
                                                                                                          'Partial '
                                                                                                          'weight '
                                                                                                          'bearing '
                                                                                                          'progression',
                                                                                                          'Weeks 4-6: '
                                                                                                          'WBAT'],
                                                                                       'rom_restrictions': ['Flexion '
                                                                                                            'limited '
                                                                                                            'to 90 '
                                                                                                            'degrees '
                                                                                                            'initially',
                                                                                                            'Emphasize '
                                                                                                            'full '
                                                                                                            'extension'],
                                                                                       'manual_therapy': ['Patellar '
                                                                                                          'mobilization',
                                                                                                          'Scar '
                                                                                                          'mobilization',
                                                                                                          'Edema '
                                                                                                          'management'],
                                                                                       'therapeutic_exercise': ['Heel '
                                                                                                                'slides',
                                                                                                                'Quad '
                                                                                                                'sets',
                                                                                                                'Patellar '
                                                                                                                'mobilization',
                                                                                                                'SLR '
                                                                                                                'all '
                                                                                                                'planes',
                                                                                                                'Gastroc '
                                                                                                                'stretching',
                                                                                                                'Gentle '
                                                                                                                'hamstring '
                                                                                                                'stretching',
                                                                                                                'Pool '
                                                                                                                'walking',
                                                                                                                'Underwater '
                                                                                                                'treadmill',
                                                                                                                'Pool '
                                                                                                                'mini-squats',
                                                                                                                'Leg '
                                                                                                                'press '
                                                                                                                '0-45 '
                                                                                                                'degrees'],
                                                                                       'criteria_to_progress': ['90 '
                                                                                                                'degrees '
                                                                                                                'flexion',
                                                                                                                'Full '
                                                                                                                'active '
                                                                                                                'extension',
                                                                                                                'Good '
                                                                                                                'quad '
                                                                                                                'set',
                                                                                                                'SLR '
                                                                                                                'without '
                                                                                                                'lag',
                                                                                                                'No '
                                                                                                                'active '
                                                                                                                'inflammation']},
                                                                'Phase II: 6-8 weeks': {'goals': ['Restore gait',
                                                                                                  'Initiate CKC '
                                                                                                  'strengthening',
                                                                                                  'Continue graft '
                                                                                                  'protection'],
                                                                                        'precautions': ['Continue '
                                                                                                        'protecting '
                                                                                                        'graft '
                                                                                                        'fixation'],
                                                                                        'brace': ['Discontinue brace '
                                                                                                  'and crutches when '
                                                                                                  'approved'],
                                                                                        'weight_bearing': ['Full '
                                                                                                           'weight '
                                                                                                           'bearing'],
                                                                                        'rom_restrictions': ['Progress '
                                                                                                             'ROM as '
                                                                                                             'tolerated'],
                                                                                        'manual_therapy': ['Soft '
                                                                                                           'tissue '
                                                                                                           'mobility',
                                                                                                           'Patellar '
                                                                                                           'mobility'],
                                                                                        'therapeutic_exercise': ['CKC '
                                                                                                                 'strengthening',
                                                                                                                 'Hamstring '
                                                                                                                 'curls',
                                                                                                                 'Aquatic '
                                                                                                                 'therapy',
                                                                                                                 'Balance '
                                                                                                                 'activities',
                                                                                                                 'Gastroc '
                                                                                                                 'stretching',
                                                                                                                 'Hamstring '
                                                                                                                 'stretching'],
                                                                                        'criteria_to_progress': ['Normalized '
                                                                                                                 'gait',
                                                                                                                 'Improved '
                                                                                                                 'strength',
                                                                                                                 'Minimal '
                                                                                                                 'swelling']},
                                                                'Phase III: 8 weeks-6 months': {'goals': ['Restore '
                                                                                                          'full ROM',
                                                                                                          'Improve '
                                                                                                          'strength',
                                                                                                          'Improve '
                                                                                                          'endurance',
                                                                                                          'Improve '
                                                                                                          'proprioception',
                                                                                                          'Prepare for '
                                                                                                          'functional '
                                                                                                          'activities'],
                                                                                                'precautions': ['Avoid '
                                                                                                                'overstressing '
                                                                                                                'graft',
                                                                                                                'Protect '
                                                                                                                'patellofemoral '
                                                                                                                'joint'],
                                                                                                'brace': ['None'],
                                                                                                'weight_bearing': ['Full'],
                                                                                                'rom_restrictions': ['Full '
                                                                                                                     'ROM'],
                                                                                                'manual_therapy': ['As '
                                                                                                                   'needed'],
                                                                                                'therapeutic_exercise': ['Stairmaster',
                                                                                                                         'Nordic '
                                                                                                                         'Track',
                                                                                                                         'Elliptical',
                                                                                                                         'Knee '
                                                                                                                         'extension '
                                                                                                                         '90-45 '
                                                                                                                         'degrees',
                                                                                                                         'Leg '
                                                                                                                         'press',
                                                                                                                         'Single-leg '
                                                                                                                         'mini '
                                                                                                                         'squats',
                                                                                                                         'Step-ups',
                                                                                                                         'Slide '
                                                                                                                         'board',
                                                                                                                         'Balance '
                                                                                                                         'activities',
                                                                                                                         'Pool '
                                                                                                                         'running',
                                                                                                                         'Swimming'],
                                                                                                'criteria_to_progress': ['Full '
                                                                                                                         'pain-free '
                                                                                                                         'ROM',
                                                                                                                         'No '
                                                                                                                         'patellofemoral '
                                                                                                                         'irritation',
                                                                                                                         'Approximately '
                                                                                                                         '70 '
                                                                                                                         'percent '
                                                                                                                         'strength',
                                                                                                                         'Physician '
                                                                                                                         'clearance']},
                                                                'Phase IV: 6-9 months': {'goals': ['Restore power',
                                                                                                   'Restore agility',
                                                                                                   'Return to '
                                                                                                   'functional '
                                                                                                   'activities',
                                                                                                   'Prepare for '
                                                                                                   'sports'],
                                                                                         'precautions': ['Gradual '
                                                                                                         'return to '
                                                                                                         'cutting and '
                                                                                                         'jumping'],
                                                                                         'brace': ['Functional brace '
                                                                                                   'if prescribed'],
                                                                                         'weight_bearing': ['Full'],
                                                                                         'rom_restrictions': ['None'],
                                                                                         'manual_therapy': ['As '
                                                                                                            'needed'],
                                                                                         'therapeutic_exercise': ['Walk/jog '
                                                                                                                  'progression',
                                                                                                                  'Forward '
                                                                                                                  'running',
                                                                                                                  'Backward '
                                                                                                                  'running',
                                                                                                                  'Cutting '
                                                                                                                  'drills',
                                                                                                                  'Carioca',
                                                                                                                  'Plyometrics',
                                                                                                                  'Sports-specific '
                                                                                                                  'drills',
                                                                                                                  'Advanced '
                                                                                                                  'agility'],
                                                                                         'criteria_to_progress': ['Physician '
                                                                                                                  'clearance',
                                                                                                                  'Successful '
                                                                                                                  'functional '
                                                                                                                  'progression',
                                                                                                                  'Return-to-sport '
                                                                                                                  'readiness']}}},
                  'ACL Reconstruction - Accelerated': {'phases': {'Phase I: Weeks 1-2': {'goals': ['ROM 0-110 degrees',
                                                                                                   'Adequate '
                                                                                                   'quadriceps '
                                                                                                   'contraction',
                                                                                                   'Control pain, '
                                                                                                   'inflammation, and '
                                                                                                   'effusion',
                                                                                                   'Progress from PWB '
                                                                                                   'to FWB'],
                                                                                         'precautions': ['Use towel '
                                                                                                         'for heel '
                                                                                                         'slides to '
                                                                                                         'avoid active '
                                                                                                         'hamstring '
                                                                                                         'contraction',
                                                                                                         'No isolated '
                                                                                                         'hamstring '
                                                                                                         'strengthening '
                                                                                                         'until week '
                                                                                                         '4'],
                                                                                         'brace': ['Brace while '
                                                                                                   'walking with '
                                                                                                   'crutches',
                                                                                                   'May remove brace '
                                                                                                   'for ROM '
                                                                                                   'activities'],
                                                                                         'weight_bearing': ['WBAT with '
                                                                                                            'crutches',
                                                                                                            'Progress '
                                                                                                            'to one '
                                                                                                            'crutch',
                                                                                                            'Progress '
                                                                                                            'to FWB '
                                                                                                            'when quad '
                                                                                                            'control '
                                                                                                            'achieved'],
                                                                                         'rom_restrictions': ['ROM '
                                                                                                              'goal '
                                                                                                              '0-110 '
                                                                                                              'degrees'],
                                                                                         'manual_therapy': ['Patellar '
                                                                                                            'mobilizations',
                                                                                                            'Edema '
                                                                                                            'management'],
                                                                                         'therapeutic_exercise': ['Passive '
                                                                                                                  'ROM',
                                                                                                                  'Ankle '
                                                                                                                  'pumps',
                                                                                                                  'Gastroc-soleus '
                                                                                                                  'stretch',
                                                                                                                  'Wall '
                                                                                                                  'slides',
                                                                                                                  'Heel '
                                                                                                                  'slides',
                                                                                                                  'Quad '
                                                                                                                  'sets',
                                                                                                                  'SLR '
                                                                                                                  'flexion',
                                                                                                                  'SLR '
                                                                                                                  'abduction',
                                                                                                                  'SLR '
                                                                                                                  'adduction',
                                                                                                                  'Multi-hip '
                                                                                                                  'machine',
                                                                                                                  'Leg '
                                                                                                                  'press '
                                                                                                                  '90-20 '
                                                                                                                  'degrees',
                                                                                                                  'Mini '
                                                                                                                  'squats '
                                                                                                                  '0-45 '
                                                                                                                  'degrees',
                                                                                                                  'Multi-angle '
                                                                                                                  'isometrics',
                                                                                                                  'Calf '
                                                                                                                  'raises',
                                                                                                                  'Weight '
                                                                                                                  'shifts',
                                                                                                                  'Single-leg '
                                                                                                                  'balance',
                                                                                                                  'Plyotoss'],
                                                                                         'criteria_to_progress': ['ROM '
                                                                                                                  '0-110',
                                                                                                                  'Good '
                                                                                                                  'quadriceps '
                                                                                                                  'control',
                                                                                                                  'Pain '
                                                                                                                  'controlled',
                                                                                                                  'Minimal '
                                                                                                                  'effusion']},
                                                                  'Phase II: Weeks 2-4': {'goals': ['Maintain full '
                                                                                                    'extension',
                                                                                                    'Increase flexion '
                                                                                                    'to 125 degrees',
                                                                                                    'Improve strength '
                                                                                                    'and endurance',
                                                                                                    'Restore '
                                                                                                    'proprioception'],
                                                                                          'precautions': ['Begin light '
                                                                                                          'hamstring '
                                                                                                          'stretching '
                                                                                                          'at week 4'],
                                                                                          'brace': ['Discontinue brace '
                                                                                                    'weeks 3-4',
                                                                                                    'Measure for '
                                                                                                    'functional brace '
                                                                                                    'at week 4'],
                                                                                          'weight_bearing': ['FWB',
                                                                                                             'Discontinue '
                                                                                                             'crutches '
                                                                                                             'when '
                                                                                                             'quad '
                                                                                                             'control '
                                                                                                             'adequate'],
                                                                                          'rom_restrictions': ['ROM '
                                                                                                               'goal '
                                                                                                               '0-125 '
                                                                                                               'degrees'],
                                                                                          'manual_therapy': ['Patellar '
                                                                                                             'mobilization',
                                                                                                             'Soft '
                                                                                                             'tissue '
                                                                                                             'mobility'],
                                                                                          'therapeutic_exercise': ['Quad '
                                                                                                                   'sets '
                                                                                                                   'with '
                                                                                                                   'biofeedback',
                                                                                                                   'SLR '
                                                                                                                   'in '
                                                                                                                   '4 '
                                                                                                                   'planes',
                                                                                                                   'Heel '
                                                                                                                   'raises',
                                                                                                                   'Toe '
                                                                                                                   'raises',
                                                                                                                   'Leg '
                                                                                                                   'press',
                                                                                                                   'Mini '
                                                                                                                   'squats',
                                                                                                                   'Front '
                                                                                                                   'lunges',
                                                                                                                   'Side '
                                                                                                                   'lunges',
                                                                                                                   'Multi-hip '
                                                                                                                   'machine',
                                                                                                                   'Bike',
                                                                                                                   'Elliptical',
                                                                                                                   'Balance '
                                                                                                                   'board',
                                                                                                                   'Cup '
                                                                                                                   'walking',
                                                                                                                   'Single-leg '
                                                                                                                   'balance',
                                                                                                                   'Plyotoss'],
                                                                                          'criteria_to_progress': ['ROM '
                                                                                                                   '0-125',
                                                                                                                   'Normal '
                                                                                                                   'gait',
                                                                                                                   'Minimal '
                                                                                                                   'swelling']},
                                                                  'Phase III: Weeks 4-12': {'goals': ['Restore full '
                                                                                                      'ROM',
                                                                                                      'Increase '
                                                                                                      'strength and '
                                                                                                      'endurance',
                                                                                                      'Restore '
                                                                                                      'functional '
                                                                                                      'capability',
                                                                                                      'Improve '
                                                                                                      'neuromuscular '
                                                                                                      'control'],
                                                                                            'precautions': ['Monitor '
                                                                                                            'swelling '
                                                                                                            'with '
                                                                                                            'progression'],
                                                                                            'brace': ['Functional '
                                                                                                      'brace as '
                                                                                                      'needed'],
                                                                                            'weight_bearing': ['Full'],
                                                                                            'rom_restrictions': ['Full '
                                                                                                                 'ROM '
                                                                                                                 'expected '
                                                                                                                 'by '
                                                                                                                 '8-12 '
                                                                                                                 'weeks'],
                                                                                            'manual_therapy': ['Stretching',
                                                                                                               'Patellar '
                                                                                                               'mobility',
                                                                                                               'Soft '
                                                                                                               'tissue '
                                                                                                               'mobility'],
                                                                                            'therapeutic_exercise': ['Hamstring '
                                                                                                                     'stretching',
                                                                                                                     'Gastroc '
                                                                                                                     'stretching',
                                                                                                                     'Single-leg '
                                                                                                                     'eccentric '
                                                                                                                     'leg '
                                                                                                                     'press',
                                                                                                                     'Hamstring '
                                                                                                                     'curls',
                                                                                                                     'Step-ups',
                                                                                                                     'Step-downs',
                                                                                                                     'Lateral '
                                                                                                                     'lunges',
                                                                                                                     'Wall '
                                                                                                                     'squats',
                                                                                                                     'Vertical '
                                                                                                                     'squats',
                                                                                                                     'Bike',
                                                                                                                     'Elliptical',
                                                                                                                     'Retro '
                                                                                                                     'treadmill',
                                                                                                                     'Straight-leg '
                                                                                                                     'deadlifts',
                                                                                                                     'Single-leg '
                                                                                                                     'stance',
                                                                                                                     'Wobble '
                                                                                                                     'board',
                                                                                                                     'Foam '
                                                                                                                     'roller '
                                                                                                                     'work',
                                                                                                                     'Jogging '
                                                                                                                     'progression '
                                                                                                                     '8-10 '
                                                                                                                     'weeks',
                                                                                                                     'Mini-tramp '
                                                                                                                     'progression',
                                                                                                                     'Walking '
                                                                                                                     'program',
                                                                                                                     'Plyometric '
                                                                                                                     'leg '
                                                                                                                     'press',
                                                                                                                     'Shuttle '
                                                                                                                     'work',
                                                                                                                     'Isokinetic '
                                                                                                                     'training'],
                                                                                            'criteria_to_progress': ['Full '
                                                                                                                     'ROM',
                                                                                                                     'Good '
                                                                                                                     'strength '
                                                                                                                     'progression',
                                                                                                                     'Minimal '
                                                                                                                     'swelling',
                                                                                                                     'Normal '
                                                                                                                     'running '
                                                                                                                     'mechanics']},
                                                                  'Phase IV: Weeks 12-16': {'goals': ['Maintain '
                                                                                                      'strength',
                                                                                                      'Improve '
                                                                                                      'neuromuscular '
                                                                                                      'control',
                                                                                                      'Progress '
                                                                                                      'sport-specific '
                                                                                                      'skills'],
                                                                                            'precautions': ['Progress '
                                                                                                            'cutting '
                                                                                                            'gradually'],
                                                                                            'brace': ['Functional '
                                                                                                      'brace as '
                                                                                                      'needed'],
                                                                                            'weight_bearing': ['Full'],
                                                                                            'rom_restrictions': ['None'],
                                                                                            'manual_therapy': ['As '
                                                                                                               'needed'],
                                                                                            'therapeutic_exercise': ['Advanced '
                                                                                                                     'plyometrics',
                                                                                                                     'Jogging '
                                                                                                                     'progression',
                                                                                                                     'Running '
                                                                                                                     'progression',
                                                                                                                     'Swimming',
                                                                                                                     'Backward '
                                                                                                                     'running',
                                                                                                                     'Sport-specific '
                                                                                                                     'drills',
                                                                                                                     'Lateral '
                                                                                                                     'movement '
                                                                                                                     'drills',
                                                                                                                     'Carioca',
                                                                                                                     'Figure-8 '
                                                                                                                     'drills'],
                                                                                            'criteria_to_progress': ['Sport-specific '
                                                                                                                     'skill '
                                                                                                                     'progression',
                                                                                                                     'Good '
                                                                                                                     'neuromuscular '
                                                                                                                     'control']},
                                                                  'Phase V: Weeks 16-36': {'goals': ['Return to '
                                                                                                     'unrestricted '
                                                                                                     'sport',
                                                                                                     'Maximize '
                                                                                                     'strength',
                                                                                                     'Maximize '
                                                                                                     'endurance',
                                                                                                     'Normalize '
                                                                                                     'neuromuscular '
                                                                                                     'control'],
                                                                                           'precautions': ['Continue '
                                                                                                           'monitoring '
                                                                                                           'swelling '
                                                                                                           'and pain'],
                                                                                           'brace': ['Functional brace '
                                                                                                     'if prescribed'],
                                                                                           'weight_bearing': ['Full'],
                                                                                           'rom_restrictions': ['None'],
                                                                                           'manual_therapy': ['As '
                                                                                                              'needed'],
                                                                                           'therapeutic_exercise': ['Advanced '
                                                                                                                    'strengthening',
                                                                                                                    'Running '
                                                                                                                    'progression',
                                                                                                                    'Swimming '
                                                                                                                    'progression',
                                                                                                                    'Plyometric '
                                                                                                                    'progression',
                                                                                                                    'Sport '
                                                                                                                    'training '
                                                                                                                    'progression',
                                                                                                                    'Neuromuscular '
                                                                                                                    'training'],
                                                                                           'criteria_to_progress': ['Return-to-sport '
                                                                                                                    'testing',
                                                                                                                    'Physician '
                                                                                                                    'clearance']}}},
                  'ACL Reconstruction - Delayed': {'phases': {'Phase I: Weeks 1-2': {'goals': ['ROM 0-90 degrees',
                                                                                               'Control pain, '
                                                                                               'inflammation, and '
                                                                                               'effusion',
                                                                                               'Adequate quadriceps '
                                                                                               'contraction',
                                                                                               'Progress weight '
                                                                                               'bearing per procedure '
                                                                                               'restrictions'],
                                                                                     'precautions': ['Meniscus Repair: '
                                                                                                     'NWB',
                                                                                                     'MCL Repair: WB '
                                                                                                     'per surgeon',
                                                                                                     'ACL Revision: '
                                                                                                     'WBAT',
                                                                                                     'Patellar '
                                                                                                     'Realignment: ROM '
                                                                                                     'limited to 0-75 '
                                                                                                     'degrees'],
                                                                                     'brace': ['I-ROM brace during '
                                                                                               'ambulation with '
                                                                                               'crutches',
                                                                                               'Remove brace for ROM '
                                                                                               'activities'],
                                                                                     'weight_bearing': ['Procedure '
                                                                                                        'dependent',
                                                                                                        'NWB to TDWB '
                                                                                                        'for meniscus '
                                                                                                        'repair',
                                                                                                        'WB per '
                                                                                                        'surgeon '
                                                                                                        'guidelines'],
                                                                                     'rom_restrictions': ['0-90 '
                                                                                                          'degrees',
                                                                                                          'Patellar '
                                                                                                          'realignment '
                                                                                                          '0-75 '
                                                                                                          'degrees'],
                                                                                     'manual_therapy': ['Patellar '
                                                                                                        'mobilizations',
                                                                                                        'Edema '
                                                                                                        'control'],
                                                                                     'therapeutic_exercise': ['Passive '
                                                                                                              'ROM',
                                                                                                              'Ankle '
                                                                                                              'pumps',
                                                                                                              'Gastroc/Soleus '
                                                                                                              'stretching',
                                                                                                              'Heel '
                                                                                                              'slides',
                                                                                                              'Wall '
                                                                                                              'slides',
                                                                                                              'Quad '
                                                                                                              'sets',
                                                                                                              'SLR '
                                                                                                              'flexion',
                                                                                                              'SLR '
                                                                                                              'abduction',
                                                                                                              'Heel '
                                                                                                              'raises',
                                                                                                              'Toe '
                                                                                                              'raises',
                                                                                                              'Wall '
                                                                                                              'squats'],
                                                                                     'criteria_to_progress': ['ROM '
                                                                                                              '0-90',
                                                                                                              'Good '
                                                                                                              'quad '
                                                                                                              'activation',
                                                                                                              'Pain '
                                                                                                              'controlled']},
                                                              'Phase II: Weeks 2-4': {'goals': ['Maintain full '
                                                                                                'extension',
                                                                                                'ROM to 90 degrees',
                                                                                                'Improve quad control',
                                                                                                'Initiate weight '
                                                                                                'bearing as permitted'],
                                                                                      'precautions': ['Continue '
                                                                                                      'procedure-specific '
                                                                                                      'restrictions'],
                                                                                      'brace': ['Continue I-ROM brace '
                                                                                                'with ambulation'],
                                                                                      'weight_bearing': ['Progress per '
                                                                                                         'surgeon '
                                                                                                         'protocol'],
                                                                                      'rom_restrictions': ['0-90 '
                                                                                                           'degrees'],
                                                                                      'manual_therapy': ['Patellar '
                                                                                                         'mobilization',
                                                                                                         'Soft tissue '
                                                                                                         'mobility'],
                                                                                      'therapeutic_exercise': ['Multi-angle '
                                                                                                               'isometrics',
                                                                                                               'Quad '
                                                                                                               'sets '
                                                                                                               'with '
                                                                                                               'biofeedback',
                                                                                                               'SLR in '
                                                                                                               'multiple '
                                                                                                               'planes',
                                                                                                               'Wall '
                                                                                                               'squats',
                                                                                                               'Heel '
                                                                                                               'raises',
                                                                                                               'Toe '
                                                                                                               'raises',
                                                                                                               'Weight '
                                                                                                               'shifts',
                                                                                                               'Single-leg '
                                                                                                               'balance '
                                                                                                               'as '
                                                                                                               'allowed'],
                                                                                      'criteria_to_progress': ['ROM '
                                                                                                               '0-90',
                                                                                                               'Improved '
                                                                                                               'quad '
                                                                                                               'control',
                                                                                                               'Reduced '
                                                                                                               'swelling']},
                                                              'Phase III: Weeks 4-6': {'goals': ['ROM to 125 degrees',
                                                                                                 'Increase LE strength',
                                                                                                 'Progress weight '
                                                                                                 'bearing',
                                                                                                 'Reduce swelling'],
                                                                                       'precautions': ['Progress WB '
                                                                                                       'gradually'],
                                                                                       'brace': ['Transition to '
                                                                                                 'functional brace'],
                                                                                       'weight_bearing': ['PWB '
                                                                                                          'progressing '
                                                                                                          'to FWB'],
                                                                                       'rom_restrictions': ['0-125 '
                                                                                                            'degrees'],
                                                                                       'manual_therapy': ['Patellar '
                                                                                                          'mobility',
                                                                                                          'Stretching'],
                                                                                       'therapeutic_exercise': ['Progressive '
                                                                                                                'isometrics',
                                                                                                                'SLR '
                                                                                                                'with '
                                                                                                                'resistance',
                                                                                                                'Heel '
                                                                                                                'raises',
                                                                                                                'Mini '
                                                                                                                'squats',
                                                                                                                'Wall '
                                                                                                                'squats',
                                                                                                                'Hamstring '
                                                                                                                'curls',
                                                                                                                'Multi-hip '
                                                                                                                'machine',
                                                                                                                'Double-leg '
                                                                                                                'eccentric '
                                                                                                                'leg '
                                                                                                                'press',
                                                                                                                'Bike '
                                                                                                                'at '
                                                                                                                '110 '
                                                                                                                'degrees '
                                                                                                                'flexion',
                                                                                                                'Elliptical',
                                                                                                                'Retro '
                                                                                                                'treadmill',
                                                                                                                'Step-ups',
                                                                                                                'Step-downs',
                                                                                                                'Lunges',
                                                                                                                'Single-leg '
                                                                                                                'stance',
                                                                                                                'Balance '
                                                                                                                'board'],
                                                                                       'criteria_to_progress': ['ROM '
                                                                                                                '0-125',
                                                                                                                'FWB '
                                                                                                                'status',
                                                                                                                'Improved '
                                                                                                                'strength']},
                                                              'Phase IV: Weeks 6-10': {'goals': ['ROM to 135 degrees',
                                                                                                 'Restore normal gait',
                                                                                                 'Improve balance',
                                                                                                 'Improve strength'],
                                                                                       'precautions': ['Monitor '
                                                                                                       'swelling'],
                                                                                       'brace': ['Functional brace as '
                                                                                                 'needed'],
                                                                                       'weight_bearing': ['Full'],
                                                                                       'rom_restrictions': ['0-135 '
                                                                                                            'degrees'],
                                                                                       'manual_therapy': ['Stretching',
                                                                                                          'Soft tissue '
                                                                                                          'mobility'],
                                                                                       'therapeutic_exercise': ['Single-leg '
                                                                                                                'eccentric '
                                                                                                                'leg '
                                                                                                                'press',
                                                                                                                'Lateral '
                                                                                                                'lunges',
                                                                                                                'Two-legged '
                                                                                                                'balance '
                                                                                                                'board',
                                                                                                                'Single-leg '
                                                                                                                'stance',
                                                                                                                'Cup '
                                                                                                                'walking',
                                                                                                                'Foam '
                                                                                                                'roller '
                                                                                                                'balance '
                                                                                                                'work'],
                                                                                       'criteria_to_progress': ['Full '
                                                                                                                'WB',
                                                                                                                'Normal '
                                                                                                                'gait',
                                                                                                                'ROM '
                                                                                                                '0-135']},
                                                              'Phase V: Weeks 10-12': {'goals': ['Restore endurance',
                                                                                                 'Improve '
                                                                                                 'proprioception',
                                                                                                 'Begin jogging '
                                                                                                 'progression'],
                                                                                       'precautions': ['Jog only if '
                                                                                                       'swelling '
                                                                                                       'minimal'],
                                                                                       'brace': ['Functional brace as '
                                                                                                 'needed'],
                                                                                       'weight_bearing': ['Full'],
                                                                                       'rom_restrictions': ['Full ROM'],
                                                                                       'manual_therapy': ['As needed'],
                                                                                       'therapeutic_exercise': ['Jogging '
                                                                                                                'progression',
                                                                                                                'Mini-tramp '
                                                                                                                'jogging',
                                                                                                                'Treadmill '
                                                                                                                'progression',
                                                                                                                'Walking '
                                                                                                                'program',
                                                                                                                'Bike '
                                                                                                                'endurance '
                                                                                                                'training',
                                                                                                                'Proprioceptive '
                                                                                                                'training'],
                                                                                       'criteria_to_progress': ['Pain-free '
                                                                                                                'jogging',
                                                                                                                'No '
                                                                                                                'swelling '
                                                                                                                'increase']},
                                                              'Phase VI: Weeks 12-16': {'goals': ['Restore functional '
                                                                                                  'confidence',
                                                                                                  'Improve strength '
                                                                                                  'and endurance',
                                                                                                  'Begin plyometric '
                                                                                                  'training'],
                                                                                        'precautions': ['Monitor '
                                                                                                        'landing '
                                                                                                        'mechanics'],
                                                                                        'brace': ['Functional brace as '
                                                                                                  'needed'],
                                                                                        'weight_bearing': ['Full'],
                                                                                        'rom_restrictions': ['Full '
                                                                                                             'ROM'],
                                                                                        'manual_therapy': ['As needed'],
                                                                                        'therapeutic_exercise': ['Plyometric '
                                                                                                                 'drills',
                                                                                                                 'Running '
                                                                                                                 'progression',
                                                                                                                 'Isokinetic '
                                                                                                                 'training'],
                                                                                        'criteria_to_progress': ['Good '
                                                                                                                 'neuromuscular '
                                                                                                                 'control',
                                                                                                                 'No '
                                                                                                                 'pain '
                                                                                                                 'with '
                                                                                                                 'plyometrics']},
                                                              'Phase VII: Weeks 16-20': {'goals': ['Improve '
                                                                                                   'sport-specific '
                                                                                                   'skills',
                                                                                                   'Advance running',
                                                                                                   'Improve '
                                                                                                   'neuromuscular '
                                                                                                   'control'],
                                                                                         'precautions': ['Progress '
                                                                                                         'cutting '
                                                                                                         'gradually'],
                                                                                         'brace': ['Functional brace '
                                                                                                   'if prescribed'],
                                                                                         'weight_bearing': ['Full'],
                                                                                         'rom_restrictions': ['None'],
                                                                                         'manual_therapy': ['As '
                                                                                                            'needed'],
                                                                                         'therapeutic_exercise': ['Advanced '
                                                                                                                  'plyometrics',
                                                                                                                  'Swimming',
                                                                                                                  'Backward '
                                                                                                                  'running',
                                                                                                                  'Sport-specific '
                                                                                                                  'drills',
                                                                                                                  'Carioca '
                                                                                                                  'drills',
                                                                                                                  'Figure-8 '
                                                                                                                  'drills',
                                                                                                                  'Lateral '
                                                                                                                  'movement '
                                                                                                                  'drills'],
                                                                                         'criteria_to_progress': ['Sport-specific '
                                                                                                                  'readiness']},
                                                              'Phase VIII: Weeks 20-36': {'goals': ['Return to '
                                                                                                    'unrestricted '
                                                                                                    'sport',
                                                                                                    'Maximize strength',
                                                                                                    'Maximize '
                                                                                                    'endurance',
                                                                                                    'Normalize '
                                                                                                    'neuromuscular '
                                                                                                    'control'],
                                                                                          'precautions': ['Continue '
                                                                                                          'gradual '
                                                                                                          'sport '
                                                                                                          'progression'],
                                                                                          'brace': ['As prescribed'],
                                                                                          'weight_bearing': ['Full'],
                                                                                          'rom_restrictions': ['None'],
                                                                                          'manual_therapy': ['As '
                                                                                                             'needed'],
                                                                                          'therapeutic_exercise': ['Advanced '
                                                                                                                   'strengthening',
                                                                                                                   'Running '
                                                                                                                   'progression',
                                                                                                                   'Swimming '
                                                                                                                   'progression',
                                                                                                                   'Plyometric '
                                                                                                                   'progression',
                                                                                                                   'Sport '
                                                                                                                   'training '
                                                                                                                   'progression',
                                                                                                                   'Neuromuscular '
                                                                                                                   'progression'],
                                                                                          'criteria_to_progress': ['Return-to-sport '
                                                                                                                   'testing',
                                                                                                                   'Physician '
                                                                                                                   'clearance']}}},
                  'MPFL Reconstruction': {'phases': {'Phase I: Immediate Post-Op (0-2 weeks)': {'goals': ['Protect '
                                                                                                          'surgical '
                                                                                                          'site',
                                                                                                          'Reduce '
                                                                                                          'swelling '
                                                                                                          'and pain',
                                                                                                          'Restore '
                                                                                                          'full '
                                                                                                          'extension',
                                                                                                          'Improve '
                                                                                                          'flexion to '
                                                                                                          'at least 90 '
                                                                                                          'degrees',
                                                                                                          'Re-establish '
                                                                                                          'quadriceps '
                                                                                                          'control',
                                                                                                          'Patient '
                                                                                                          'education'],
                                                                                                'precautions': ['Avoid '
                                                                                                                'resting '
                                                                                                                'with '
                                                                                                                'towel '
                                                                                                                'under '
                                                                                                                'knee',
                                                                                                                'Protect '
                                                                                                                'reconstruction',
                                                                                                                'Monitor '
                                                                                                                'swelling '
                                                                                                                'and '
                                                                                                                'effusion'],
                                                                                                'brace': ['Brace '
                                                                                                          'locked '
                                                                                                          'initially',
                                                                                                          'Unlock per '
                                                                                                          'surgeon '
                                                                                                          'protocol'],
                                                                                                'weight_bearing': ['PWB '
                                                                                                                   'first '
                                                                                                                   'week',
                                                                                                                   'Progress '
                                                                                                                   'to '
                                                                                                                   'WBAT '
                                                                                                                   'with '
                                                                                                                   'crutches',
                                                                                                                   'Discontinue '
                                                                                                                   'crutches '
                                                                                                                   'once '
                                                                                                                   'gait '
                                                                                                                   'normal '
                                                                                                                   'and '
                                                                                                                   'pain '
                                                                                                                   'controlled'],
                                                                                                'rom_restrictions': ['Restore '
                                                                                                                     'full '
                                                                                                                     'extension',
                                                                                                                     'Flexion '
                                                                                                                     'goal '
                                                                                                                     '90+ '
                                                                                                                     'degrees'],
                                                                                                'manual_therapy': ['Retrograde '
                                                                                                                   'massage',
                                                                                                                   'Edema '
                                                                                                                   'management',
                                                                                                                   'Compression',
                                                                                                                   'Elevation'],
                                                                                                'therapeutic_exercise': ['Ankle '
                                                                                                                         'pumps',
                                                                                                                         'PROM',
                                                                                                                         'Heel '
                                                                                                                         'slides '
                                                                                                                         'with '
                                                                                                                         'towel',
                                                                                                                         'Prone '
                                                                                                                         'hangs',
                                                                                                                         'Heel '
                                                                                                                         'props',
                                                                                                                         'Hamstring '
                                                                                                                         'stretch',
                                                                                                                         'Calf '
                                                                                                                         'stretch',
                                                                                                                         'Calf '
                                                                                                                         'raises',
                                                                                                                         'Quad '
                                                                                                                         'sets',
                                                                                                                         'NMES '
                                                                                                                         'if '
                                                                                                                         'indicated',
                                                                                                                         'SLR '
                                                                                                                         'progression'],
                                                                                                'criteria_to_progress': ['SLR '
                                                                                                                         'without '
                                                                                                                         'lag',
                                                                                                                         'Full '
                                                                                                                         'extension',
                                                                                                                         'Minimal '
                                                                                                                         'swelling']},
                                                     'Phase II: Intermediate (3-6 weeks)': {'goals': ['Protect '
                                                                                                      'surgical site',
                                                                                                      'Restore full '
                                                                                                      'flexion',
                                                                                                      'Normalize gait',
                                                                                                      'Maintain full '
                                                                                                      'extension'],
                                                                                            'precautions': ['Avoid '
                                                                                                            'excessive '
                                                                                                            'patellofemoral '
                                                                                                            'stress'],
                                                                                            'brace': ['May unlock when '
                                                                                                      'SLR without lag',
                                                                                                      'Discontinue '
                                                                                                      'brace at 6 '
                                                                                                      'weeks when gait '
                                                                                                      'normalized'],
                                                                                            'weight_bearing': ['WBAT'],
                                                                                            'rom_restrictions': ['Restore '
                                                                                                                 'full '
                                                                                                                 'ROM'],
                                                                                            'manual_therapy': ['Patellar '
                                                                                                               'mobilization '
                                                                                                               'if '
                                                                                                               'stiffness '
                                                                                                               'present'],
                                                                                            'therapeutic_exercise': ['Stationary '
                                                                                                                     'bike',
                                                                                                                     'Ball '
                                                                                                                     'squeezes',
                                                                                                                     'SLR '
                                                                                                                     'adduction',
                                                                                                                     'Bridges '
                                                                                                                     'with '
                                                                                                                     'ball '
                                                                                                                     'squeeze',
                                                                                                                     'Wall '
                                                                                                                     'slides',
                                                                                                                     'Mini '
                                                                                                                     'squats '
                                                                                                                     '0-60 '
                                                                                                                     'degrees',
                                                                                                                     'Single-leg '
                                                                                                                     'balance'],
                                                                                            'criteria_to_progress': ['No '
                                                                                                                     'swelling',
                                                                                                                     'Flexion '
                                                                                                                     'greater '
                                                                                                                     'than '
                                                                                                                     '90 '
                                                                                                                     'degrees',
                                                                                                                     'Extension '
                                                                                                                     'equal '
                                                                                                                     'to '
                                                                                                                     'contralateral '
                                                                                                                     'side']},
                                                     'Phase III: Late Post-Op (7-12 weeks)': {'goals': ['Maintain full '
                                                                                                        'ROM',
                                                                                                        'Progress '
                                                                                                        'strengthening',
                                                                                                        'Improve '
                                                                                                        'movement '
                                                                                                        'patterns',
                                                                                                        'Improve '
                                                                                                        'proprioception'],
                                                                                              'precautions': ['Avoid '
                                                                                                              'post-exercise '
                                                                                                              'pain or '
                                                                                                              'swelling'],
                                                                                              'brace': ['None'],
                                                                                              'weight_bearing': ['FWB '
                                                                                                                 'without '
                                                                                                                 'assistive '
                                                                                                                 'device'],
                                                                                              'rom_restrictions': ['Full '
                                                                                                                   'ROM'],
                                                                                              'manual_therapy': ['As '
                                                                                                                 'needed'],
                                                                                              'therapeutic_exercise': ['Prone '
                                                                                                                       'quad '
                                                                                                                       'stretch',
                                                                                                                       'Standing '
                                                                                                                       'quad '
                                                                                                                       'stretch',
                                                                                                                       'Hip '
                                                                                                                       'flexor '
                                                                                                                       'stretch',
                                                                                                                       'Elliptical',
                                                                                                                       'Stair '
                                                                                                                       'climber',
                                                                                                                       'Pool '
                                                                                                                       'jogging',
                                                                                                                       'Flutter '
                                                                                                                       'kick '
                                                                                                                       'swimming',
                                                                                                                       'Leg '
                                                                                                                       'press',
                                                                                                                       'Hamstring '
                                                                                                                       'curls',
                                                                                                                       'Hip '
                                                                                                                       'abductor '
                                                                                                                       'machine',
                                                                                                                       'Hip '
                                                                                                                       'adductor '
                                                                                                                       'machine',
                                                                                                                       'Hip '
                                                                                                                       'extension '
                                                                                                                       'machine',
                                                                                                                       'Calf '
                                                                                                                       'machine',
                                                                                                                       'Lateral '
                                                                                                                       'band '
                                                                                                                       'walks',
                                                                                                                       'Perturbation '
                                                                                                                       'balance '
                                                                                                                       'training'],
                                                                                              'criteria_to_progress': ['Normal '
                                                                                                                       'gait',
                                                                                                                       'ROM '
                                                                                                                       'equal '
                                                                                                                       'to '
                                                                                                                       'contralateral '
                                                                                                                       'side',
                                                                                                                       'Quad/Hamstring/Glute '
                                                                                                                       'index '
                                                                                                                       'at '
                                                                                                                       'least '
                                                                                                                       '70 '
                                                                                                                       'percent']},
                                                     'Phase IV: Transitional (13-16 weeks)': {'goals': ['Maintain full '
                                                                                                        'ROM',
                                                                                                        'Progress '
                                                                                                        'strengthening',
                                                                                                        'Improve '
                                                                                                        'landing '
                                                                                                        'mechanics',
                                                                                                        'Prepare for '
                                                                                                        'running'],
                                                                                              'precautions': ['Avoid '
                                                                                                              'pain-producing '
                                                                                                              'activities'],
                                                                                              'brace': ['None'],
                                                                                              'weight_bearing': ['Full'],
                                                                                              'rom_restrictions': ['None'],
                                                                                              'manual_therapy': ['As '
                                                                                                                 'needed'],
                                                                                              'therapeutic_exercise': ['Advanced '
                                                                                                                       'strengthening',
                                                                                                                       'Single-leg '
                                                                                                                       'balance',
                                                                                                                       'Perturbation '
                                                                                                                       'training',
                                                                                                                       'Bilateral '
                                                                                                                       'plyometrics',
                                                                                                                       'Single-leg '
                                                                                                                       'plyometrics'],
                                                                                              'criteria_to_progress': ['Quad/Hamstring/Glute '
                                                                                                                       'index '
                                                                                                                       'at '
                                                                                                                       'least '
                                                                                                                       '80 '
                                                                                                                       'percent',
                                                                                                                       'Hop '
                                                                                                                       'testing '
                                                                                                                       'at '
                                                                                                                       'least '
                                                                                                                       '80 '
                                                                                                                       'percent',
                                                                                                                       'Good '
                                                                                                                       'landing '
                                                                                                                       'mechanics',
                                                                                                                       'Physician '
                                                                                                                       'clearance']},
                                                     'Phase V: Early Return to Sport (3-5 months)': {'goals': ['Initiate '
                                                                                                               'sport-specific '
                                                                                                               'training',
                                                                                                               'Improve '
                                                                                                               'strength '
                                                                                                               'and '
                                                                                                               'power',
                                                                                                               'Begin '
                                                                                                               'running '
                                                                                                               'progression'],
                                                                                                     'precautions': ['Avoid '
                                                                                                                     'graft '
                                                                                                                     'donor '
                                                                                                                     'site '
                                                                                                                     'pain',
                                                                                                                     'Monitor '
                                                                                                                     'swelling'],
                                                                                                     'brace': ['None'],
                                                                                                     'weight_bearing': ['Full'],
                                                                                                     'rom_restrictions': ['None'],
                                                                                                     'manual_therapy': ['As '
                                                                                                                        'needed'],
                                                                                                     'therapeutic_exercise': ['Return-to-running '
                                                                                                                              'program',
                                                                                                                              'Strength '
                                                                                                                              'progression',
                                                                                                                              'Sport-specific '
                                                                                                                              'drills',
                                                                                                                              'Plyometric '
                                                                                                                              'progression'],
                                                                                                     'criteria_to_progress': ['KOOS '
                                                                                                                              'Sports '
                                                                                                                              'greater '
                                                                                                                              'than '
                                                                                                                              '90',
                                                                                                                              'IKDC '
                                                                                                                              'greater '
                                                                                                                              'than '
                                                                                                                              '93',
                                                                                                                              'PRRS '
                                                                                                                              'greater '
                                                                                                                              'than '
                                                                                                                              '90',
                                                                                                                              'Kujala '
                                                                                                                              'greater '
                                                                                                                              'than '
                                                                                                                              '90']},
                                                     'Phase VI: Unrestricted Return to Sport (6+ months)': {'goals': ['Return '
                                                                                                                      'to '
                                                                                                                      'unrestricted '
                                                                                                                      'sport',
                                                                                                                      'Restore '
                                                                                                                      'full '
                                                                                                                      'performance',
                                                                                                                      'Maintain '
                                                                                                                      'strength '
                                                                                                                      'and '
                                                                                                                      'power'],
                                                                                                            'precautions': ['Continue '
                                                                                                                            'symptom '
                                                                                                                            'monitoring'],
                                                                                                            'brace': ['None'],
                                                                                                            'weight_bearing': ['Full'],
                                                                                                            'rom_restrictions': ['None'],
                                                                                                            'manual_therapy': ['As '
                                                                                                                               'needed'],
                                                                                                            'therapeutic_exercise': ['Multi-plane '
                                                                                                                                     'plyometrics',
                                                                                                                                     'Agility '
                                                                                                                                     'progression',
                                                                                                                                     'Hard '
                                                                                                                                     'cutting '
                                                                                                                                     'drills',
                                                                                                                                     'Pivoting '
                                                                                                                                     'drills',
                                                                                                                                     'Full '
                                                                                                                                     'practice '
                                                                                                                                     'progression',
                                                                                                                                     'Return-to-play '
                                                                                                                                     'progression'],
                                                                                                            'criteria_to_progress': ['Quad/Hamstring/Glute '
                                                                                                                                     'index '
                                                                                                                                     'at '
                                                                                                                                     'least '
                                                                                                                                     '90 '
                                                                                                                                     'percent',
                                                                                                                                     'Hamstring/Quad '
                                                                                                                                     'ratio '
                                                                                                                                     'at '
                                                                                                                                     'least '
                                                                                                                                     '70 '
                                                                                                                                     'percent',
                                                                                                                                     'Hop '
                                                                                                                                     'testing '
                                                                                                                                     'at '
                                                                                                                                     'least '
                                                                                                                                     '90 '
                                                                                                                                     'percent',
                                                                                                                                     'KOOS '
                                                                                                                                     'Sports '
                                                                                                                                     'greater '
                                                                                                                                     'than '
                                                                                                                                     '90',
                                                                                                                                     'IKDC '
                                                                                                                                     'greater '
                                                                                                                                     'than '
                                                                                                                                     '93',
                                                                                                                                     'ACL-RSI '
                                                                                                                                     'acceptable',
                                                                                                                                     'Physician '
                                                                                                                                     'clearance']}}},
                  'Total Knee Replacement': {'phases': {'Phase I: 0-2 weeks': {'goals': ['Control pain and swelling',
                                                                                         'Restore knee extension',
                                                                                         'Improve knee flexion',
                                                                                         'Activate quadriceps',
                                                                                         'Improve safe gait with '
                                                                                         'assistive device'],
                                                                               'precautions': ['Monitor incision',
                                                                                               'Monitor excessive '
                                                                                               'swelling',
                                                                                               'Avoid placing pillow '
                                                                                               'under knee for '
                                                                                               'prolonged periods',
                                                                                               'Watch for signs of DVT '
                                                                                               'or infection'],
                                                                               'brace': ['None unless prescribed'],
                                                                               'weight_bearing': ['WBAT unless '
                                                                                                  'otherwise '
                                                                                                  'instructed'],
                                                                               'rom_restrictions': ['Emphasize full '
                                                                                                    'knee extension',
                                                                                                    'Progress knee '
                                                                                                    'flexion as '
                                                                                                    'tolerated'],
                                                                               'manual_therapy': ['Patellar '
                                                                                                  'mobilizations',
                                                                                                  'Scar mobility when '
                                                                                                  'incision healed',
                                                                                                  'Edema management',
                                                                                                  'PROM/AAROM knee '
                                                                                                  'flexion and '
                                                                                                  'extension'],
                                                                               'therapeutic_exercise': ['Ankle pumps',
                                                                                                        'Quad sets',
                                                                                                        'Glute sets',
                                                                                                        'Heel slides',
                                                                                                        'Short arc '
                                                                                                        'quads',
                                                                                                        'SLR if no '
                                                                                                        'quad lag',
                                                                                                        'Seated knee '
                                                                                                        'flexion',
                                                                                                        'LAQ as '
                                                                                                        'tolerated',
                                                                                                        'Gait training',
                                                                                                        'Stair '
                                                                                                        'training as '
                                                                                                        'appropriate'],
                                                                               'criteria_to_progress': ['Pain '
                                                                                                        'controlled',
                                                                                                        'Improved quad '
                                                                                                        'activation',
                                                                                                        'Improving '
                                                                                                        'knee ROM',
                                                                                                        'Safe '
                                                                                                        'ambulation '
                                                                                                        'with '
                                                                                                        'assistive '
                                                                                                        'device']},
                                                        'Phase II: 2-6 weeks': {'goals': ['Improve ROM',
                                                                                          'Normalize gait mechanics',
                                                                                          'Increase quadriceps and hip '
                                                                                          'strength',
                                                                                          'Improve balance',
                                                                                          'Improve functional '
                                                                                          'mobility'],
                                                                                'precautions': ['Avoid excessive '
                                                                                                'post-treatment '
                                                                                                'swelling',
                                                                                                'Monitor pain '
                                                                                                'response'],
                                                                                'brace': ['None'],
                                                                                'weight_bearing': ['WBAT',
                                                                                                   'Progress away from '
                                                                                                   'assistive device '
                                                                                                   'as safe'],
                                                                                'rom_restrictions': ['Progress toward '
                                                                                                     'functional ROM'],
                                                                                'manual_therapy': ['Patellar '
                                                                                                   'mobilizations',
                                                                                                   'Tibiofemoral '
                                                                                                   'mobilizations as '
                                                                                                   'appropriate',
                                                                                                   'Soft tissue '
                                                                                                   'mobilization',
                                                                                                   'Scar mobilization '
                                                                                                   'when healed'],
                                                                                'therapeutic_exercise': ['Bike rocking',
                                                                                                         'Stationary '
                                                                                                         'bike',
                                                                                                         'Mini squats',
                                                                                                         'Step-ups',
                                                                                                         'Sit-to-stands',
                                                                                                         'Terminal '
                                                                                                         'knee '
                                                                                                         'extensions',
                                                                                                         'Standing hip '
                                                                                                         'strengthening',
                                                                                                         'Calf raises',
                                                                                                         'Hamstring '
                                                                                                         'curls',
                                                                                                         'Balance '
                                                                                                         'training',
                                                                                                         'Gait '
                                                                                                         'training'],
                                                                                'criteria_to_progress': ['Improved '
                                                                                                         'gait quality',
                                                                                                         'Improved ROM',
                                                                                                         'Good '
                                                                                                         'tolerance to '
                                                                                                         'strengthening',
                                                                                                         'Reduced '
                                                                                                         'assistive '
                                                                                                         'device '
                                                                                                         'dependence']},
                                                        'Phase III: 6-12 weeks': {'goals': ['Restore functional '
                                                                                            'strength',
                                                                                            'Improve endurance',
                                                                                            'Improve stair negotiation',
                                                                                            'Improve balance and '
                                                                                            'community ambulation'],
                                                                                  'precautions': ['Progress '
                                                                                                  'strengthening '
                                                                                                  'gradually',
                                                                                                  'Monitor swelling '
                                                                                                  'after activity'],
                                                                                  'brace': ['None'],
                                                                                  'weight_bearing': ['Full'],
                                                                                  'rom_restrictions': ['Functional ROM '
                                                                                                       'expected'],
                                                                                  'manual_therapy': ['Manual therapy '
                                                                                                     'as needed for '
                                                                                                     'ROM limitations',
                                                                                                     'Soft tissue '
                                                                                                     'mobility as '
                                                                                                     'needed'],
                                                                                  'therapeutic_exercise': ['Leg press',
                                                                                                           'Step-downs',
                                                                                                           'Lateral '
                                                                                                           'stepping',
                                                                                                           'Resisted '
                                                                                                           'hip '
                                                                                                           'strengthening',
                                                                                                           'Progressive '
                                                                                                           'squats',
                                                                                                           'Single-leg '
                                                                                                           'balance',
                                                                                                           'Treadmill '
                                                                                                           'walking',
                                                                                                           'Bike',
                                                                                                           'Elliptical '
                                                                                                           'if '
                                                                                                           'tolerated',
                                                                                                           'Functional '
                                                                                                           'lifting '
                                                                                                           'mechanics'],
                                                                                  'criteria_to_progress': ['Independent '
                                                                                                           'gait or '
                                                                                                           'least '
                                                                                                           'restrictive '
                                                                                                           'device',
                                                                                                           'Improved '
                                                                                                           'stair '
                                                                                                           'function',
                                                                                                           'Improved '
                                                                                                           'functional '
                                                                                                           'strength',
                                                                                                           'Independent '
                                                                                                           'with '
                                                                                                           'HEP']}}}},
         'Ankle': {},
         'Foot': {}}}
