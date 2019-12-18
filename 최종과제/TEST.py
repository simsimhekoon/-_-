from ClassficationUtil import ClassficationUtil

AI = ClassficationUtil()

AI.read('output.csv')
AI.show()
AI.heatmap()
AI.run_svm(['Day2','Money'], 'Place')
AI.run_neighbor_classifier(['Day2','Money'], 'Place', 3)
AI.run_logistic_regression(['Day2','Money'], 'Place')
AI.run_decision_tree_classifier(['Day2','Money'], 'Place')