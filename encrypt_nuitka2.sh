# Скрипт сборки модуля core
nuitka3 --module core --include-package=core --remove-output --no-pyi-file --follow-import-to=core

for f in $(find core/ -name "*.py")
do
 rm $f
done
