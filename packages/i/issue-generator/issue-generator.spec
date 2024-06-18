#
# spec file for package issue-generator
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


Name:           issue-generator
Version:        1.13
Release:        0
Summary:        Generates an issue files from different snippets
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/thkukuk/issue-generator
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
Requires(post): %fillup_prereq
BuildArch:      noarch

%description
issue-generator is a tool to create an issue file dynamically.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}
%ifarch s390x
# Adjust regex in sysconfig/issue-generator for s390x
sed -i -e 's|NETWORK_INTERFACE_REGEX=.*|NETWORK_INTERFACE_REGEX="^[beqich]"|g' udev/sysconfig.issue-generator
%endif

%install
%make_install
mkdir -p %{buildroot}%{_fillupdir}
install -m 644 udev/sysconfig.issue-generator %{buildroot}%{_fillupdir}/
%fdupes %{buildroot}%{_mandir}

%pre
%service_add_pre issue-generator.service issue-generator.path issue-add-ssh-keys.service

%post
%tmpfiles_create issue-generator.conf
%{fillup_only -n issue-generator}
%service_add_post issue-generator.service issue-generator.path issue-add-ssh-keys.service

%preun
%service_del_preun issue-generator.service issue-generator.path issue-add-ssh-keys.service

%postun
%service_del_postun issue-generator.service issue-generator.path issue-add-ssh-keys.service

%files
%license COPYING
%doc NEWS README.md
%dir %{_sysconfdir}/issue.d
%dir %{_prefix}/lib/issue.d
%dir %{_prefix}/lib/tmpfiles.d
%dir %{_prefix}/lib/udev
%dir %{_prefix}/lib/udev/rules.d
%{_fillupdir}/sysconfig.issue-generator
%{_prefix}/lib/tmpfiles.d/issue-generator.conf
%{_prefix}/lib/udev/rules.d/90-issue-generator.rules
%{_prefix}/lib/systemd/system/issue-add-ssh-keys.service
%{_prefix}/lib/systemd/system/issue-generator.path
%{_prefix}/lib/systemd/system/issue-generator.service
%{_sbindir}/issue-generator
%{_mandir}/man5/issue.d.5%{ext_man}
%{_mandir}/man8/issue-generator.8%{ext_man}
%{_mandir}/man8/90-issue-generator.rules.8%{ext_man}
%{_mandir}/man8/issue-add-ssh-keys.service.8%{ext_man}
%{_mandir}/man8/issue-generator.conf.8%{ext_man}
%{_mandir}/man8/issue-generator.service.8%{ext_man}

%changelog
