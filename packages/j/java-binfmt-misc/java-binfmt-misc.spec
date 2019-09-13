#
# spec file for package java-binfmt-misc
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           java-binfmt-misc
Version:        1.4
Release:        0
Summary:        The binfmt_misc support for Java
License:        GPL-2.0
Group:          Development/Languages/Java
Url:            http://www.kernel.org/
# derived from Linux's Documentation/java.txt
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  update-desktop-files
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(post): systemd
Requires(postun): desktop-file-utils
Requires(postun): shared-mime-info
Requires(postun): systemd
# split-alias for libzypp
Provides:       jpackage-utils:%{_bindir}/jarwrapper

%description
Linux beats them ALL! While all other OS's are TALKING about direct
support of Java Binaries in the OS, Linux is doing it!

You can execute Java applications and Java Applets just like any other
program after you have installed this package.

%prep
%setup -q

%build
gcc %{optflags} javaclassname.c -o javaclassname

%install
# a basic directory structure
install -d -m 0755 %{buildroot}/%{_datadir}/{applications,pixmaps}
install -d -m 0755 %{buildroot}/%{_libexecdir}/binfmt.d
install -d -m 0755 %{buildroot}/%{_bindir}/
install -d -m 0755 %{buildroot}/%{_mandir}/man1
# wrappers
install -m 0755 javaclassname %{buildroot}/%{_bindir}/
install -m 0755 *wrapper %{buildroot}/%{_bindir}/
# desktop menu
install -m 0644 share/java.png %{buildroot}%{_datadir}/pixmaps/java.png
install -m 0644 share/*desktop %{buildroot}%{_datadir}/applications/
for wrapper in jarwrapper javawrapper javawswrapper; do
    # init binfmt.d snippet
    install -m 0644 ${wrapper}.conf %{buildroot}%{_libexecdir}/binfmt.d/
    %suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/$wrapper.desktop Technology Java
done
# manual page
mv docs/%{name}.1 %{buildroot}/%{_mandir}/man1
(
cd %{buildroot}/%{_mandir}/man1
for alias in jarwrapper javawrapper javawswrapper javaclassname; do
    ln -sf %{name}.1 $alias.1
done
)

%post
%desktop_database_post
%mime_database_post
%{_bindir}/systemctl restart systemd-binfmt.service ||:

%postun
%desktop_database_postun
%mime_database_postun
%{_bindir}/systemctl restart systemd-binfmt.service ||:

%files
%doc docs/
%attr(755,root,root) %{_bindir}/*
# Avoid dependency on systemd
%dir %{_libexecdir}/binfmt.d/
%{_libexecdir}/binfmt.d/*.conf
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/*

%changelog
