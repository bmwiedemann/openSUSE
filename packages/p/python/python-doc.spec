#
# spec file for package python-doc
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-doc
Version:        2.7.18
Release:        0
Summary:        Additional Package Documentation for Python
License:        Python-2.0
Group:          Development/Languages/Python
URL:            http://www.python.org/
%define         tarname Python-%{version}
Source0:        %{tarname}.tar.xz
# docs for current version are regenerated every day
# this messes with autobuild "file changed" checks
#Source2:        http://docs.python.org/%{version}/archives/python-%{pyver}-docs-pdf-a4.tar.bz2
#Source3:        http://docs.python.org/%{version}/archives/python-%{pyver}-docs-pdf-letter.tar.bz2
Source2:        python-%{version}-docs-pdf-a4.tar.bz2
Source3:        python-%{version}-docs-pdf-letter.tar.bz2
%if 0%{?suse_version} >= 1500
BuildRequires:  python3-Sphinx
%else
BuildRequires:  python-Sphinx
%endif
BuildRequires:  xz
# COMMON-PATCH-BEGIN
Patch1:         python-2.7-dirs.patch
Patch2:         python-distutils-rpm-8.patch
Patch3:         python-2.7.5-multilib.patch
Patch4:         python-2.5.1-sqlite.patch
Patch5:         python-2.7.4-canonicalize2.patch
Patch7:         python-2.6-gettext-plurals.patch
Patch8:         python-2.6b3-curses-panel.patch
Patch10:        sparc_longdouble.patch
Patch13:        python-2.7.2-fix_date_time_compiler.patch
Patch17:        remove-static-libpython.patch
# PATCH-FEATURE-OPENSUSE python-bundle-lang.patch bnc#617751 dimstar@opensuse.org -- gettext: when looking in default_localedir also check in locale-bundle.
Patch20:        python-bundle-lang.patch
# PATCH-FIX-UPSTREAM Fix argument passing in libffi for aarch64
Patch22:        python-2.7-libffi-aarch64.patch
Patch24:        python-bsddb6.patch
# PATCH-FIX-UPSTREAM accept directory-based CA paths as well
Patch33:        python-2.7.9-ssl_ca_path.patch
# PATCH-FEATURE-SLE disable SSL verification-by-default in http clients
Patch34:        python-2.7.9-sles-disable-verification-by-default.patch
# PATCH-FIX-UPSTREAM do not use non-ASCII filename in test_ssl.py
Patch35:        do-not-use-non-ascii-in-test_ssl.patch
# PATCH-FIX-UPSTREAM bmwiedemann@suse.de -- allow python packages to build reproducibly
Patch38:        reproducible.patch
# bypass boo#1078485 random failing tests
Patch40:        python-skip_random_failing_tests.patch
# PATCH-FIX-UPSTREAM sorted tar https://github.com/python/cpython/pull/2263
Patch41:        python-sorted_tar.patch
# https://github.com/python/cpython/pull/9624 (https://bugs.python.org/issue34834)
Patch47:        openssl-111-middlebox-compat.patch
# PATCH-FIX-SUSE python default SSLContext doesn't contain OP_CIPHER_SERVER_PREFERENCE
Patch48:        openssl-111-ssl_options.patch
# PATCH-FIX-UPSTREAM CVE-2019-5010-null-defer-x509-cert-DOS.patch bnc#1122191 mcepl@suse.com
# gh#python/cpython#11569
# Fix segfault in ssl's cert parser
Patch49:        CVE-2019-5010-null-defer-x509-cert-DOS.patch
# PATCH-FIX-UPSTREAM bpo36160-init-sysconfig_vars.patch gh#python/cpython#12131 mcepl@suse.com
# Initialize sysconfig variables in test_site.
Patch50:        bpo36160-init-sysconfig_vars.patch
# PATCH-FIX-UPSTREAM CVE-2017-18207.patch gh#python/cpython#4437 psimons@suse.com
# Add check for channels of wav file in Lib/wave.py
Patch51:        CVE-2017-18207.patch
# PATCH-FIX-UPSTREAM gh#python/cpython#12341
Patch55:        bpo36302-sort-module-sources.patch
# Fix installation in /usr/local (boo#1071941), adapted from Fedora
# https://src.fedoraproject.org/rpms/python3/blob/master/f/00251-change-user-install-location.patch
# Set values of prefix and exec_prefix in distutils install command
# to /usr/local if executable is /usr/bin/python* and RPM build
# is not detected to make pip and distutils install into separate location
Patch56:        adapted-from-F00251-change-user-install-location.patch
# Switch couple of tests failing on acient SLE-12
Patch57:        python-2.7.17-switch-off-failing-SSL-tests.patch
# PATCH-FIX-UPSTREAM CVE-2020-8492-urllib-ReDoS.patch bsc#1162367 mcepl@suse.com
# Fixes Python urrlib allowed an HTTP server to conduct Regular
# Expression Denial of Service (ReDoS)
Patch58:        CVE-2020-8492-urllib-ReDoS.patch
# PATCH-FIX-UPSTREAM CVE-2019-9674-zip-bomb.patch bsc#1162825 mcepl@suse.com
# Improve documentation warning against the possible zip bombs
Patch59:        CVE-2019-9674-zip-bomb.patch
# PATCH-FIX-UPSTREAM configure_PYTHON_FOR_REGEN.patch bsc#1078326 mcepl@suse.com
# PYTHON_FOR_REGEN value is set very weird upstream
Patch60:        configure_PYTHON_FOR_REGEN.patch
# COMMON-PATCH-END
Provides:       pyth_doc
Provides:       pyth_ps
Obsoletes:      pyth_doc
Obsoletes:      pyth_ps
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Enhances:       python = %{version}
Provides:       python2-doc = %{version}

%description
Tutorial, Global Module Index, Language Reference, Library Reference,
Extending and Embedding Reference, Python/C API Reference, Documenting
Python, and Macintosh Module Reference in HTML format.

%package pdf
Summary:        Python PDF Documentation
Group:          Development/Languages/Python
Provides:       pyth_pdf
Obsoletes:      pyth_pdf
Provides:       python2-doc-pdf = %{version}

%description pdf
Tutorial, Global Module Index, Language Reference, Library Reference,
Extending and Embedding Reference, Python/C API Reference, Documenting
Python, and Macintosh Module Reference in PDF format.

%prep
%setup -q -n %{tarname}
# COMMON-PREP-BEGIN
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch10 -p1
%patch13 -p1
%patch17 -p1
%patch20 -p1
%patch22 -p1
%patch24 -p1
%patch33 -p1
%if %{suse_version} == 1315 && !0%{?is_opensuse}
%patch34 -p1
%endif
%patch35 -p1
%patch38 -p1
%ifarch ppc ppc64 ppc64le
%patch40 -p1
%endif
%patch41 -p1
%if %{suse_version} >= 1500
%patch47 -p1
%patch48 -p1
%else
%patch57 -p1
%endif
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch55 -p1
%patch56 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1

# drop Autoconf version requirement
sed -i 's/^version_required/dnl version_required/' configure.ac
# COMMON-PREP-END

%build
TODAY_DATE=`date -r %{S:0} "+%B %d, %Y"`
# TODO use not date of tarball but date of latest patch

pushd Doc
sed -i "s/^today = .*/today = '$TODAY_DATE'/" conf.py
%if 0%{?suse_version} < 1320
# lower sphinx version requirement, docs seem to work fine with 1.1
sed -i "s/^needs_sphinx = .*/needs_sphinx = '1.1'/" conf.py
%endif
make html
popd

%install
export PDOCS=%{buildroot}%{_docdir}/python
install -d -m 755 $PDOCS/Misc
rm Doc/build/html/.buildinfo
mv Doc/build/html $PDOCS/html
tar xfj %{SOURCE2} -C $PDOCS
mv $PDOCS/docs-pdf $PDOCS/paper-a4
tar xfj %{SOURCE3} -C $PDOCS
mv $PDOCS/docs-pdf $PDOCS/paper-letter
# this is part of main package
#install -c -m 644 README $PDOCS/README 
for i in Misc/* ; do
  [ -f $i ] && install -c -m 644 $i $PDOCS/Misc/
done

%files
%defattr(644,root,root,755)
%dir %{_docdir}/python
%doc %{_docdir}/python/Misc
%doc %{_docdir}/python/html
#%doc %{_docdir}/python/README

%files pdf
%defattr(644,root,root,755)
%doc %{_docdir}/python/paper-a4
%doc %{_docdir}/python/paper-letter

%changelog
