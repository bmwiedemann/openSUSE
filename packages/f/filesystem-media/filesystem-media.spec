#
# spec file for package filesystem-media
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           filesystem-media
Version:        0.1
Release:        0
Summary:        Polyinstantiated /media Directory
License:        CC0-1.0
Group:          System/Fhs
Source1:        %{name}.README
Source2:        %{name}.init
Source3:        %{name}-rpmlintrc
Requires:       acl
Requires(post): pam
#Supplements:    udisks2
BuildArch:      noarch

%description
The Filesystem Hierarchy Standard defines /media as a directory for removable
media. This package provides an udisks compatible /media directory.

%prep
%setup -q -c -T
cp %{SOURCE1} README
cp %{SOURCE2} .

%build

%install
mkdir %{buildroot}/media
mkdir -p %{buildroot}%{_sysconfdir}/security/namespace.d
install %{name}.init %{buildroot}%{_sysconfdir}/security/namespace.d/

%triggerin -- pam xdm gdm util-linux lxdm sddm
RC=0
# Activate pam_namespace in PAM configuration.
for PAM_FILE in xdm xdm-np gdm gdm-autologin lightdm-greeter lxdm sddm sddm-autologin login ; do
	if ! test -f %{_sysconfdir}/pam.d/$PAM_FILE ; then
		continue
	fi
	CMNT=
	if grep -q '^[^#]*pam_namespace.so' %{_sysconfdir}/pam.d/$PAM_FILE ; then
		if ! grep '^[^#]*pam_namespace.so' %{_sysconfdir}/pam.d/$PAM_FILE | grep -q ignore_instance_parent_mode ; then
			RC=1
			echo >&2 "filesystem-media needs to install pam_namespace.so module with option ignore_instance_parent_mode.
But file %{_sysconfdir}/pam.d/$PAM_FILE already contains pam_namespace.so without this argument.
Please fix and uncomment line inside filesystem-media comments!"
			CMNT="#"
		fi
	fi
	sed -i '/^#BEGIN filesystem-media/,/^#END filesystem-media/d' %{_sysconfdir}/pam.d/$PAM_FILE
	sed -i '$a\
#BEGIN filesystem-media\
'"${CMNT}"'session  required       pam_namespace.so ignore_instance_parent_mode\
#END filesystem-media' %{_sysconfdir}/pam.d/$PAM_FILE
done
exit $RC

%post
# Configure pam_namespace to handle /media.
sed -i '/^#BEGIN filesystem-media/,/^#END filesystem-media/d' %{_sysconfdir}/security/namespace.conf
sed -i '$a\
#BEGIN filesystem-media\
/media   /run/media/           context:iscript=%{name}.init\
#END filesystem-media' %{_sysconfdir}/security/namespace.conf

%preun
if test $1 -eq 0 ; then
	umount /media/* >/dev/null 2>/dev/null || :
	umount /media >/dev/null 2>/dev/null || :
fi

%postun
if test $1 -eq 0 ; then
	sed -i '/^#BEGIN filesystem-media/,/^#END filesystem-media/d' %{_sysconfdir}/security/namespace.conf
	for PAM_FILE in xdm gdm gdm-autologin login ; do
		if ! test -f %{_sysconfdir}/pam.d/$PAM_FILE ; then
			continue
		fi
		sed -i '/^#BEGIN filesystem-media/,/^#END filesystem-media/d' %{_sysconfdir}/pam.d/$PAM_FILE
	done
fi

%files
%doc README
/media
%{_sysconfdir}/security/namespace.d/%{name}.init
# FIXME: should be owned by pam
%dir %{_sysconfdir}/security/namespace.d

%changelog
