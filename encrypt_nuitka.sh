# Скрипт шифрования проекта
for f in $(cat encrypt_files.txt)
do
  echo $f
  nuitka3 --module --output-dir=$(dirname $f)  --remove-output --no-pyi-file $f
  rm $f
done