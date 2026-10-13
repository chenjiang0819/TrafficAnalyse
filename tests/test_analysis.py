import ast,json,unittest,io,contextlib
from pathlib import Path
from unittest.mock import patch
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
NB=json.loads((Path(__file__).resolve().parents[1]/'project.ipynb').read_text())
SOURCES=[''.join(c['source']) for c in NB['cells'] if c['cell_type']=='code']
class AnalysisTests(unittest.TestCase):
 def test_seeded_missing_data_alignment(self):
  frame=pd.DataFrame(np.random.RandomState(3).rand(1200,19),columns=['id']+['feature'+str(i) for i in range(18)])
  frame['feature3']=frame['feature3'].astype(object)
  frame['StrType']=np.where(frame.index%2,'Arterial','Local');frame.loc[::7,'feature3']='-'
  source=next(s for s in SOURCES if '#Q3.2 a' in s)
  results=[]
  for _ in range(2):
   scope={'pd':pd,'np':np,'plt':plt}
   with patch.object(pd,'read_csv',return_value=frame.copy()),patch.object(plt,'show'),contextlib.redirect_stdout(io.StringIO()):exec(source,scope)
   self.assertEqual(scope['specffic'].index.tolist(),scope['special_traffic'].index.tolist());self.assertEqual(len(scope['colors']),len(scope['tra_sklearn']));results.append(scope['tra_sklearn']);plt.close('all')
  np.testing.assert_array_equal(*results)
 def test_training_only_heldout_surrogate(self):
  seen=[]
  class AuditedPCA(PCA):
   def fit(self,X,y=None):seen.append(set(X.index));return super().fit(X,y)
  scope=dict(np=np,train_test_split=train_test_split,sklearnPCA=AuditedPCA,KMeans=KMeans,KNeighborsClassifier=KNeighborsClassifier)
  source=next(s for s in SOURCES if 'def heldout_cluster_agreement' in s);tree=ast.parse(source);tree.body=[x for x in tree.body if isinstance(x,ast.FunctionDef)];exec(compile(tree,'notebook','exec'),scope)
  features=pd.DataFrame(np.random.RandomState(4).rand(120,18))
  a=scope['heldout_cluster_agreement'](features);b=scope['heldout_cluster_agreement'](features)
  train,test=train_test_split(features,test_size=.33333,random_state=2026)
  self.assertEqual(seen[0],set(train.index));self.assertTrue(seen[0].isdisjoint(test.index));self.assertEqual(a,b);self.assertEqual(a[1]+a[2],120);self.assertTrue(0<=a[0]<=1)
if __name__=='__main__':unittest.main()
