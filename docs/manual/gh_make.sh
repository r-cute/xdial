declare -a lang_ls=("en" "zh-cn")

for lang in "${lang_ls[@]}"
do
	sphinx-build -b html -d ${lang}/_build/doctrees ${lang} ${1}/${lang}
done