# macros.perl file
# macros for perl module building. handle with care.

# Useful perl macros (from Artur Frysiak <wiget@t17.ds.pwr.wroc.pl>)
#
%perl_sitearch   %(eval "`%{__perl} -V:installsitearch`"; echo $installsitearch)
%perl_sitelib    %(eval "`%{__perl} -V:installsitelib`"; echo $installsitelib)
%perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%perl_vendorlib  %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%perl_archlib    %(eval "`%{__perl} -V:installarchlib`"; echo $installarchlib)
%perl_privlib    %(eval "`%{__perl} -V:installprivlib`"; echo $installprivlib)

# More useful perl macros (from Raul Dias <rsd@swi.com.br>)
#
%perl_version           %(perl -V:version | sed "s!.*='!!;s!'.*!!")
%perl_man1ext           %(perl -V:man1ext | sed "s!.*='!!;s!'.*!!")
%perl_man3ext           %(perl -V:man3ext | sed "s!.*='!!;s!'.*!!")
%perl_man1dir           %(perl -V:man1dir | sed "s!.*='!!;s!'.*!!")
%perl_man3dir           %(perl -V:man3dir | sed "s!.*='!!;s!'.*!!")
%perl_installman1dir    %(perl -V:installman1dir | sed "s!.*='!!;s!'.*!!")
%perl_installman3dir    %(perl -V:installman3dir | sed "s!.*='!!;s!'.*!!")
%perl_installarchlib    %(perl -V:installarchlib | sed "s!.*='!!;s!'.*!!")
%perl_prefix            %{buildroot}

# Macro to encapsulate perl requires (empty for fedora)
# we keep the complicated form even here to easy sync the other macros with
# perl-macros package
# 
%perl_requires() \
%if 0%{?suse_version} > 0 \
Requires: perl(:MODULE_COMPAT_%{perl_version}) \
%endif

%libperl_requires() \
%if 0%{?suse_version} > 0 \
Requires: perl = %{perl_version} \
%endif

# suse specific macros
#
%perl_make_install make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist(n:) \
  if test -n "$RPM_BUILD_ROOT" -a -d $RPM_BUILD_ROOT%perl_vendorarch/auto; then \
    find $RPM_BUILD_ROOT%perl_vendorarch/auto -name .packlist -print0 | xargs -0 -r rm \
    if [ %{_target_cpu} == noarch ]; then \
      find $RPM_BUILD_ROOT%perl_vendorarch/auto -depth -type d -print0 | xargs -0 -r rmdir \
    fi \
  fi \
  rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod \
  %nil

# macro: perl_gen_filelist (from Christian <chris@computersalat.de>)
# do the rpmlint happy filelist generation
# with %dir in front of directories
#
%perl_gen_filelist(n)\
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
# check for files in %{perl_vendorlib}\
RES=`find ${RPM_BUILD_ROOT}%{perl_vendorlib} -maxdepth 1 -type f`\
if [ -n "$RES" ]; then\
  for file in $RES; do\
    fgen_file "%{perl_vendorlib}/$(basename ${file})"\
  done\
fi\
\
# get all dirs into array\
base_dir="${RPM_BUILD_ROOT}%{perl_vendorlib}/"\
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
  # do not add "dir {perl_vendorlib/arch}/auto", included in perl package\
  if [ "${i}" = "auto" ]; then\
    continue\
  fi\
  if [ "%{perl_vendorlib}/${i}" = "%{perl_vendorarch}/auto" ]; then\
    continue\
  else\
    if [ -d ${base_dir}/${i} ]; then\
      if [ "%{perl_vendorlib}/${i}" != "%{perl_vendorarch}" ]; then\
        fgen_dir "%{perl_vendorlib}/${i}"\
      fi\
      RES=`find "${base_dir}/${i}" -maxdepth 1 -type f`\
      for file in $RES; do\
        fgen_file "%{perl_vendorlib}/${i}/$(basename ${file})"\
      done\
    fi\
  fi\
done\
# add man pages\
# if exist :)\
if [ -d "${RPM_BUILD_ROOT}%{_mandir}" ]; then\
for file in `cd "${RPM_BUILD_ROOT}%{_mandir}" && find . -type f -name "*3pm*"`; do \
   if test -e "%{_mandir}/$file" -o -e "%{_mandir}/$file.gz"; then \
     mv ${RPM_BUILD_ROOT}%{_mandir}/$file ${RPM_BUILD_ROOT}%{_mandir}/${file/3pm/3pmc} \
   fi \
done \
fgen_file "%{_mandir}/man?/*"\
fi\
\
# add packlist file\
# generated fom perllocal.pod\
if [ -f "${RPM_BUILD_ROOT}/var/adm/perl-modules/%{name}" ]; then\
  fgen_file "/var/adm/perl-modules/%{name}"\
fi\
\
# check for files in %{_bindir}\
if [ -d ${RPM_BUILD_ROOT}%{_bindir} ]; then\
  RES=`find "${RPM_BUILD_ROOT}%{_bindir}" -maxdepth 1 -type f`\
  if [ -n "$RES" ]; then\
    for file in $RES; do\
      fgen_file "%{_bindir}/$(basename ${file})"\
    done\
  fi\
fi
