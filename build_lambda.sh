mkdir lambda_env/
cp -r src/* lambda_env/
pip install -r env/py/requirements.txt -t lambda_env/
cd lambda_env/
zip -r lambda_scrape_akibasouken.zip ./*
mv lambda_scrape_akibasouken.zip ../
cd ..
rm -r lambda_env/