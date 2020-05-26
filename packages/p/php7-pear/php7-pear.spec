#
# spec file for package php7-pear
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


%global peardir %{_datadir}/php7/PEAR
%global metadir %{_localstatedir}/lib/pear

%define pear_module_version(m) %(sed -n 's/.*=>.*%{1}-\\(.*\\)\\.tar.*/\\1/p' %{SOURCE0})

Name:           php7-pear
Version:        1.10.19
Release:        0
Summary:        PHP Extension and Application Repository
License:        BSD-2-Clause
Group:          Development/Libraries/PHP
URL:            https://pear.php.net/package/pearweb_phars
Source0:        https://github.com/pear/pearweb_phars/raw/v%{version}/install-pear-nozlib.phar
Source1:        https://github.com/pear/pearweb_phars/raw/v%{version}/install-pear-nozlib.sig#/install-pear-nozlib.phar.sig
Source2:        %{name}.keyring
Source3:        %{name}.rpmlintrc
BuildRequires:  php7
Requires:       php7
Recommends:     php7-openssl
Provides:       php-pear = %{version}
Provides:       php-pear(Archive_Tar) = %pear_module_version Archive_Tar
Provides:       php-pear(Console_Getopt) = %pear_module_version Console_Getopt
Provides:       php-pear(PEAR) = %pear_module_version PEAR
Provides:       php-pear(Structures_Graph) = %pear_module_version Structures_Graph
Provides:       php-pear(XML_Util) = %pear_module_version XML_Util
Obsoletes:      php-pear < %{version}
%if 0%{?suse_version} <= 1500 
Provides:       php7-pear-Archive_Tar
Obsoletes:      php7-pear-Archive_Tar
%endif
BuildArch:      noarch

%description
PEAR is a code repository for PHP extensions and PHP library code
similar to TeX's CTAN and Perl's CPAN. This package provides an access
to the repository.

See https://pear.php.net/manual for more details.

%package -n php7-pecl
Summary:        PHP Extension Community Library
Group:          Development/Libraries/PHP
Requires:       autoconf
Requires:       automake
Requires:       gcc-c++
Requires:       libtool
Requires:       php7-pear = %{version}
Provides:       php-pecl = %{version}
Obsoletes:      php-pecl < %{version}
Conflicts:      php7-devel < 7.4
BuildArch:      noarch

%description -n php7-pecl
PECL is a repository for PHP Extensions, providing a directory of
all known extensions and hosting facilities for downloading and
development of PHP extensions.

See https://pecl.php.net for more details.

%prep
# Empty prep section, nothing to prepare

%build
# Empty build section, nothing to build

%install
export PHP_PEAR_INSTALL_DIR=%{peardir}
export PHP_PEAR_METADATA_DIR=%{metadir}
export PHP_PEAR_SIG_BIN=%{_bindir}/gpg
export PHP_PEAR_SYSCONF_DIR=%{_sysconfdir}/php7/cli
export INSTALL_ROOT=%{buildroot}

install -d %{buildroot}%{_localstatedir}/{cache,lib}/pear

php -d date.timezone=UTC -d memory_limit=64M -d short_open_tag=0 -d safe_mode=0 \
	-d 'error_reporting=E_ALL&~E_DEPRECATED' -d detect_unicode=0 %{SOURCE0} \
	--force \
	--bin      %{_bindir} \
	--cache    %{_localstatedir}/cache/pear \
	--dir      %{peardir} \
	--man      %{_mandir} \
	--metadata %{metadir} \
	--www      %{peardir}/htdocs

%pre
if [ -d %{peardir}/.registry -a ! -d %{metadir}/.registry ]; then
    mkdir -p %{metadir}
    cp -af %{peardir}/{.channels,.registry} %{metadir}
fi

%posttrans
mdir=$(%{_bindir}/pear config-get metadata_dir system)
if [ "${mdir}" != "%{metadir}" -a -d %{metadir}/.registry ]; then
    %{_bindir}/pear config-set metadata_dir %{metadir} system
    rm -rf %{peardir}/{.channels,.registry}
fi

%files
%{_bindir}/pear
%config(noreplace) %{_sysconfdir}/php7/cli/pear.conf
%dir %{_localstatedir}/cache/pear
%dir %{_localstatedir}/lib/pear
%dir %{peardir}
%docdir %{peardir}/doc
%{peardir}/*
%{metadir}/.??*
%exclude %{_bindir}/peardev
%exclude %{peardir}/doc/PEAR/INSTALL
%exclude %{peardir}/test

%files -n php7-pecl
%{_bindir}/pecl

%changelog
