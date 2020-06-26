# Automatic-Test-Generation

For webserver you need to install following packages:
```
pip install django
pip install fuzzywuzzy
```

For the model part follow this steps:
```
cd qg
mkdir bert-cased-pretrained-cache
mkdir data
cd data
wget https://drive.google.com/open?id=1JN2wnkSRotwUnJ_Z-AbWwoPdP53Gcfsn
cd ..
pip install --user tensorboardX six numpy tqdm path.py pandas scikit-learn lmdb pyarrow py-lz4framed methodtools py-rouge pyrouge nltk
python -c "import nltk; nltk.download('punkt')"
pip install -e git://github.com/Maluuba/nlg-eval.git#egg=nlg-eval
git clone https://github.com/microsoft/unilm.git
cd unilm/unilm-v1/src
pip install --user --editable .
```

Running the webserver:
```
cd backend
python manage.py runserver 0.0.0.0:21210
```

Running the server with model:
```
cd qg
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=1234
```
