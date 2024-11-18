#
# spec file for package icingaweb2
#
# Copyright (c) 2024 SUSE LLC
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


%define php_major_version 8
Name:           icingaweb2
Version:        2.12.2
Release:        0
Summary:        Icinga Web
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://icinga.com
Source0:        https://github.com/Icinga/icingaweb2/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        icingaweb2-additions.tar.gz
Source10:       %{name}-php-fpm.conf
Source90:       README.SUSE
Source99:       %{name}-rpmlintrc
BuildRequires:  apache2
BuildRequires:  nagios-rpm-macros
Requires:       apache2
Requires:       icinga-l10n >= 1.1.0
Requires:       icingacli = %{version}
Requires:       icingaweb2-common = %{version}
Requires:       php-icinga = %{version}
Requires:       (mod_php_any or php-fpm)
Provides:       group(%icinga_command_group)
Recommends:     icingaweb2-module-pdfexport >= 0.10
BuildArch:      noarch

%description
Lightweight and extensible web interface to tackle your monitoring challenge.

%package common
Summary:        Common files for Icinga Web and the Icinga CLI
PreReq:         permissions
Requires(pre):  shadow
Provides:       group(%icinga_webgroup)

%description common
Manages common files for Icinga Web and the Icinga CLI.

%package -n icingacli
Summary:        Icinga CLI
Requires:       bash-completion
Requires:       icinga-l10n >= 1.1.0
Requires:       icingaweb2-common = %{version}
Requires:       php-cli
Requires:       php-icinga = %{version}

%description -n icingacli
Icinga command line interface.

%package php-fpm
Summary:        PHP FPM configuration for %{name}
Group:          Productivity/Networking/Web/Utilities
BuildRequires:  php%{php_major_version}-fpm
Requires:       %{name} = %{version}
%requires_eq    php%{php_major_version}-fpm

%description php-fpm
This package contains the PHP FPM configuration file to run %{name} with php-fpm.

%package -n php-icinga
Summary:        Icinga Web PHP library
Group:          Development/Libraries/Other
Requires:       icinga-php-library >= 0.13.0
Requires:       icinga-php-thirdparty >= 0.12.0
Requires:       php-curl
Requires:       php-dom
Requires:       php-fileinfo
Requires:       php-gd
Requires:       php-gettext
Requires:       php-intl
Requires:       php-json
Requires:       php-ldap
Requires:       php-mbstring
Requires:       php-openssl
Requires:       php-pdo
Requires:       php-pdo_mysql
Requires:       php-pdo_pgsql
Requires:       php-posix
Requires:       php-xml
Obsoletes:      php-Icinga < %{version}
Provides:       php-Icinga = %{version}
Obsoletes:      icingaweb2-vendor-HTMLPurifier < %{version}
Provides:       icingaweb2-vendor-HTMLPurifier = %{version}
Obsoletes:      icingaweb2-vendor-JShrink < %{version}
Provides:       icingaweb2-vendor-JShrink = %{version}
Obsoletes:      icingaweb2-vendor-Parsedown < %{version}
Provides:       icingaweb2-vendor-Parsedown = %{version}
Obsoletes:      icingaweb2-vendor-dompdf < %{version}
Provides:       icingaweb2-vendor-dompdf = %{version}
Obsoletes:      icingaweb2-vendor-lessphp < %{version}
Provides:       icingaweb2-vendor-lessphp = %{version}
Obsoletes:      icingaweb2-vendor-zf1 < %{version}
Provides:       icingaweb2-vendor-zf1 = %{version}

%description -n php-icinga
Icinga Web PHP and vendor libraries.

%prep
%autosetup -a1

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
cp -pr application doc library modules public schema %{buildroot}%{_datadir}/%{name}
install -dm 0770 %{buildroot}%{_sysconfdir}/%{name}
install -dm 2770 %{buildroot}%{_sysconfdir}/%{name}/enabledModules
install -dm 0770 %{buildroot}%{_sysconfdir}/%{name}/modules
install -Dpm 0644 etc/bash_completion.d/icingacli %{buildroot}%{_datadir}/bash-completion/completions/icingacli
cp -p additions/index.php %{buildroot}%{_datadir}/%{name}/public
install -d %{buildroot}%{_datadir}/php
mv %{buildroot}%{_datadir}/%{name}/library/Icinga %{buildroot}%{_datadir}/php
install -dm 770 %{buildroot}%{_localstatedir}/cache/%{name} %{buildroot}%{_localstatedir}/lib/%{name}
install -dm 775 %{buildroot}%{_localstatedir}/log/%{name}
install -Dpm 0644 additions/icingaweb2.conf %{buildroot}%{_sysconfdir}/apache2/conf.d/icingaweb2.conf
install -Dpm 0755 additions/icingacli %{buildroot}%{_bindir}/icingacli
# fpm
mkdir -p %{buildroot}%{_sysconfdir}/php%{php_major_version}/fpm/php-fpm.d
cp -avL %{SOURCE10} %{buildroot}%{_sysconfdir}/php%{php_major_version}/fpm/php-fpm.d/%{name}.conf

%pre
getent group %icinga_command_group >/dev/null || groupadd -r %icinga_command_group
usermod -a -G %icinga_command_group,%icinga_webgroup %icinga_command_user

%pre common
getent group %icinga_webgroup  >/dev/null || groupadd -r %icinga_webgroup

%verifyscript common
# TODO: Maybe the others are needed after all?
#%%verify_permissions -e %%{_sysconfdir}/%%{name}
%verify_permissions -e %{_sysconfdir}/%{name}/enabledModules
%verify_permissions -e %{_sysconfdir}/%{name}/modules
#%%verify_permissions -e %%{_localstatedir}/cache/%%{name}
#%%verify_permissions -e %%{_localstatedir}/lib/%%{name}
#%%verify_permissions -e %%{_localstatedir}/log/%%{name}

%post common
# TODO: Maybe the others are needed after all?
#%%set_permissions %%{_sysconfdir}/%%{name}
%set_permissions %{_sysconfdir}/%{name}/enabledModules
%set_permissions %{_sysconfdir}/%{name}/modules
#%%set_permissions %%{_localstatedir}/cache/%%{name}
#%%set_permissions %%{_localstatedir}/lib/%%{name}
#%%set_permissions %%{_localstatedir}/log/%%{name}

%files
%doc CHANGELOG.md
%doc README.md
%docdir %{_datadir}/%{name}/doc
%license LICENSE
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/application
%{_datadir}/%{name}/application/controllers
%{_datadir}/%{name}/application/fonts
%{_datadir}/%{name}/application/forms
%{_datadir}/%{name}/application/layouts
%{_datadir}/%{name}/application/views
%{_datadir}/%{name}/application/VERSION
%{_datadir}/%{name}/doc
%{_datadir}/%{name}/modules
%{_datadir}/%{name}/public
%{_datadir}/%{name}/schema
%config(noreplace) %{_sysconfdir}/apache2/conf.d/icingaweb2.conf

%files common
%attr(0770, root, %icinga_webgroup) %dir %{_localstatedir}/cache/%{name}
%attr(0775, root, %icinga_webgroup) %dir %{_localstatedir}/log/%{name}
%attr(0770, root, %icinga_webgroup) %dir %{_localstatedir}/lib/%{name}
%attr(0770, root, %icinga_webgroup) %config(noreplace) %dir %{_sysconfdir}/%{name}
%attr(0770, root, %icinga_webgroup) %config(noreplace) %dir %{_sysconfdir}/%{name}/modules
%verify(not mode caps) %attr(2770,root,%icinga_webgroup) %{_sysconfdir}/%{name}/enabledModules
%attr(2770, root, %icinga_webgroup) %dir %{_sysconfdir}/%{name}/enabledModules

%files -n icingacli
%license LICENSE
%{_datadir}/%{name}/application/clicommands
%{_datadir}/bash-completion/completions/icingacli
%{_bindir}/icingacli

%files php-fpm
%config(noreplace) %{_sysconfdir}/php%{php_major_version}/fpm/php-fpm.d/%{name}.conf

%files -n php-icinga
%license LICENSE
%{_datadir}/php/Icinga

%changelog
