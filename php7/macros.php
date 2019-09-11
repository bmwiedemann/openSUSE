# macros.php file
# macros for module building. handle with care.

#
# Interface versions exposed by PHP:
#
%php_core_api @PHP_APIVER@
%php_zend_api @PHP_ZENDVER@

# Useful php macros (from Christian Wittmer <chris@computersalat.de>)
#
%__php          /usr/bin/php
%__phpize       /usr/bin/phpize
%__php_config   /usr/bin/php-config
%php_version    %(%{__php_config} --version)

# pear related macros
%__pear         /usr/bin/pear
%php_peardir    %(%{__pear} config-get php_dir)

# %pear_xmldir should be replaced by %php_pearxmldir
%pear_xmldir /var/lib/pear

%php_pearxmldir /var/lib/pear
%pear_phpdir  %(%{__pear} config-get php_dir  2> /dev/null || echo undefined)
%pear_docdir  %(%{__pear} config-get doc_dir  2> /dev/null || echo undefined)
%pear_testdir %(%{__pear} config-get test_dir 2> /dev/null || echo undefined)
%pear_datadir %(%{__pear} config-get data_dir 2> /dev/null || echo undefined)
%pear_cfgdir  %(%{__pear} config-get cfg_dir  2> /dev/null || echo undefined)
%pear_wwwdir  %(%{__pear} config-get www_dir  2> /dev/null || echo undefined)
%pear_metadir %(%{__pear} config-get metadata_dir 2> /dev/null || echo undefined)

# pecl related macros
%__pecl       /usr/bin/pecl
%pecl_phpdir  %(%{__pecl} config-get php_dir  2> /dev/null || echo undefined)
%pecl_docdir  %(%{__pecl} config-get doc_dir  2> /dev/null || echo undefined)
%pecl_testdir %(%{__pecl} config-get test_dir 2> /dev/null || echo undefined)
%pecl_datadir %(%{__pecl} config-get data_dir 2> /dev/null || echo undefined)

# macro: php_pear_gen_filelist
# do the rpmlint happy filelist generation
# with %dir in front of directories
%php_pear_gen_filelist(n)\
FILES=%{name}.files\
# fgen_dir func\
# IN: dir\
fgen_dir(){\
%{__cat} >> $FILES << EOF\
%dir ${1}\
EOF\
}\
# fgen_file func\
# IN: file\
fgen_file(){\
%{__cat} >> $FILES << EOF\
${1}\
EOF\
}\
# check for files in %{php_peardir}\
RES=`find ${RPM_BUILD_ROOT}%{php_peardir} -maxdepth 1 -type f`\
if [ -n "$RES" ]; then\
  for file in $RES; do\
    fgen_file "%{php_peardir}/$(basename ${file})"\
  done\
fi\
\
# get all dirs into array\
base_dir="${RPM_BUILD_ROOT}%{php_peardir}/"\
for dir in `find ${base_dir} -type d | sort`; do\
  if [ "$dir" = "${base_dir}" ]; then\
    continue\
  else\
    el=`echo $dir | %{__awk} -F"${base_dir}" '{print $2}'`\
    all_dir=(${all_dir[@]} $el)\
  fi\
done\
\
# build filelist\
for i in ${all_dir[@]}; do\
  if [ -d ${base_dir}/${i} ]; then\
    RES=`find "${base_dir}/${i}" -maxdepth 1 -type f`\
    if [ -n "$RES" ]; then\
      fgen_dir "%{php_peardir}/${i}"\
      for file in $RES; do\
        fgen_file "%{php_peardir}/${i}/$(basename ${file})"\
      done\
    else\
      fgen_dir "%{php_peardir}/${i}"\
    fi\
  fi\
done\
# add xml file\
fgen_file "%php_pearxmldir/%{pear_name}.xml"\
#
