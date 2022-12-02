#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%global app_name cepces
%global selinux_variants targeted
%global logdir %{_localstatedir}/log/%{app_name}

Name:           %{app_name}
Version:        0.3.7
Release:        0%{?dist}
Summary:        Certificate Enrollment through CEP/CES

License:        GPL-3.0-or-later
URL:            https://github.com/ufven/%{app_name}
Source0:        %{name}-%{version}.tar.bz2
BuildArch:      noarch

Requires:       %{app_name}-certmonger == %{version}
Requires:       python3-%{app_name} == %{version}
%if 0%{?sle_version} > 150400 || 0%{?suse_version} > 1500
Requires:       (%{app_name}-selinux == %{version} if selinux-policy)
%endif

%description
%{app_name} is an application for enrolling certificates through CEP and CES.
It currently only operates through certmonger.

%package -n python3-%{app_name}
Summary:        Python part of %{app_name}

BuildRequires:  python3-cryptography >= 1.2
BuildRequires:  python3-devel
BuildRequires:  python3-requests
BuildRequires:  python3-requests-gssapi
BuildRequires:  python3-setuptools

Requires:       python3-cryptography >= 1.2
Requires:       python3-requests
Requires:       python3-requests-gssapi

%description -n python3-%{app_name}
%{app_name} is an application for enrolling certificates through CEP and CES.
This package provides the Python part for CEP and CES interaction.

%package certmonger
Summary:        certmonger integration for %{app_name}

Requires:       %{name} == %{version}
Requires:       certmonger

%description certmonger
%{app_name} is an application for enrolling certificates through CEP and CES.
This package provides the certmonger integration.

%if 0%{?sle_version} > 150400 || 0%{?suse_version} > 1500
%package selinux
Summary:        SELinux support for %{app_name}

BuildRequires:  selinux-policy-devel

Requires:       selinux-policy
Requires(post): selinux-policy-targeted

%description selinux
SELinux support for %{app_name}
%endif

%prep
%setup -q -n %{app_name}-%{version}

%build
%py3_build

%if 0%{?sle_version} > 150400 || 0%{?suse_version} > 1500
# Build the SELinux module(s).
for SELINUXVARIANT in %{selinux_variants}; do
  make -C selinux clean all
  mv -v selinux/%{app_name}.pp selinux/%{app_name}-${SELINUXVARIANT}.pp
done
%endif

%install
%py3_install

install -d -m 0700 %{buildroot}%{logdir}

%if 0%{?sle_version} > 150400 || 0%{?suse_version} > 1500
# Install the SELinux module(s).
rm -fv selinux-files.txt

for SELINUXVARIANT in %{selinux_variants}; do
  install -d %{buildroot}%{_datadir}/selinux/${SELINUXVARIANT}
  install -p -m 644 selinux/%{app_name}-${SELINUXVARIANT}.pp \
    %{buildroot}%{_datadir}/selinux/${SELINUXVARIANT}/%{app_name}.pp

  echo %{_datadir}/selinux/${SELINUXVARIANT}/%{app_name}.pp >> \
    selinux-files.txt
done
%endif

# Install configuration files.
install -d %{buildroot}%{_sysconfdir}/%{app_name}
install -p -m 644 conf/cepces.conf.dist \
  %{buildroot}%{_sysconfdir}/%{app_name}/cepces.conf
install -p -m 644 conf/logging.conf.dist \
  %{buildroot}%{_sysconfdir}/%{app_name}/logging.conf

install -d %{buildroot}%{_libexecdir}/certmonger
install -p -m 755 bin/%{app_name}-submit \
  %{buildroot}%{_libexecdir}/certmonger/%{app_name}-submit

# Remove unused executables and configuration files.
%{__rm} -rfv %{buildroot}/usr/local/etc
%{__rm} -rfv %{buildroot}/usr/local/libexec/certmonger

sed -i 's/\/usr\/bin\/env python3/\/usr\/bin\/python3/g' %{buildroot}%{_libexecdir}/certmonger/%{app_name}-submit

%if 0%{?sle_version} > 150400 || 0%{?suse_version} > 1500
%post selinux
for SELINUXVARIANT in %{selinux_variants}; do
  %{_sbindir}/semodule -n -s ${SELINUXVARIANT} \
    -i %{_datadir}/selinux/${SELINUXVARIANT}/%{app_name}.pp

  if %{_sbindir}/selinuxenabled; then
    %{_sbindir}/load_policy
  fi
done

%postun selinux
if [ $1 -eq 0 ]
then
  for SELINUXVARIANT in %{selinux_variants}; do
    %{_sbindir}/semodule -n -s ${SELINUXVARIANT} -r %{app_name} > /dev/null || :

    if %{_sbindir}/selinuxenabled; then
      %{_sbindir}/load_policy
    fi
  done
fi
%endif

%post certmonger
# Install the CA into certmonger.
if [ $1 -eq 1 ]; then
  getcert add-ca -c %{app_name} \
    -e %{_libexecdir}/certmonger/%{app_name}-submit >/dev/null || :
fi

%preun certmonger
# Remove the CA from certmonger, unless it's an upgrade.
if [ $1 -eq 0 ]; then
  getcert remove-ca -c %{app_name} >/dev/null || :
fi

%check
pushd tests
%{__python3} ./runner.py
popd

%files
%doc README.rst
%dir %{_sysconfdir}/%{app_name}/
%config(noreplace) %{_sysconfdir}/%{app_name}/%{app_name}.conf
%config(noreplace) %{_sysconfdir}/%{app_name}/logging.conf
%dir %{logdir}

%files -n python3-%{app_name}
%license LICENSE
%{python3_sitelib}/%{app_name}
%{python3_sitelib}/%{app_name}-%{version}-py*.egg-info

%files certmonger
%dir %{_libexecdir}/certmonger
%{_libexecdir}/certmonger/%{app_name}-submit

%if 0%{?sle_version} > 150400 || 0%{?suse_version} > 1500
%files selinux -f selinux-files.txt
%defattr(0644,root,root,0755)
%endif

%changelog
