#
# spec file for package openSUSE-signkey-cert
#
# Copyright (c) 2021 SUSE LLC
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
# needssslcertforbuild


%define startdate %(openssl x509 -in %{_sourcedir}/_projectcert.crt -inform PEM -noout -startdate | cut -d= -f 2)
%define version %(echo "$(date --date="%{startdate}" +'%Y%m%d')")
Name:           openSUSE-signkey-cert
Version:        %{version}
Release:        0
Summary:        Certificate for openSUSE KMP signing key
License:        GPL-2.0-or-later
Group:          System/Kernel
BuildRequires:  openssl >= 0.9.8
Requires(post): mokutil
# matches mokutil
ExclusiveArch:  x86_64 aarch64 ppc64le ppc64

%description
This package includes the certificate of openSUSE signing key for signing
kernel module file (.ko) in openSUSE KMP. This package also calls mokutil
to help user to enroll certificate to MOK. Then kernel module in openSUSE
KMP can be verified by kernel.

%build
openssl x509 -in %{_sourcedir}/_projectcert.crt -outform DER -out kmp-key.der

%install
install -d %{buildroot}/%{_sysconfdir}/uefi/certs/
fpr=$(openssl x509 -sha1 -fingerprint -inform DER -noout -in kmp-key.der | cut -c 18- | cut -d ":" -f 1,2,3,4 | sed 's/://g')
install -m 644 kmp-key.der %{buildroot}/%{_sysconfdir}/uefi/certs/${fpr}-kmp.crt

%files
%dir %{_sysconfdir}/uefi/
%dir %{_sysconfdir}/uefi/certs/
%{_sysconfdir}/uefi/certs/*.crt

%post
if command -v mokutil >/dev/null; then
	# enroll all *-kmp.crt certificates
	# the mokutil import command will auto-skip enrolled certificates
	certs=$(ls %{_sysconfdir}/uefi/certs/*-kmp.crt 2>/dev/null || true)
	for cert in $certs
	do
		if ! mokutil --import "$cert" --root-pw; then
			echo "Failed to import $cert"
		fi
	done
fi
exit 0

%preun
if command -v mokutil >/dev/null; then
	# copy all existing *-kmp.crt to *-kmp.crt.del as backup files
	# for using by mokutil --delete
	# those *-kmp.crt.del will be handled in postun
	certs=$(ls %{_sysconfdir}/uefi/certs/*-kmp.crt 2>/dev/null || true)
	for cert in $certs
	do
		cp "$cert" "$cert.del"
	done
fi
exit 0

%postun
if command -v mokutil >/dev/null; then
	# surviving certificate do not need to be deleted by mokutil
	# so, remove the -kmp.crt.del file
	certs=$(ls %{_sysconfdir}/uefi/certs/*-kmp.crt 2>/dev/null || true)
	for cert in $certs
	do
		rm "$cert.del"
	done
	# using -kmp.crt.del file to remove mok
	del_certs=$(ls %{_sysconfdir}/uefi/certs/*-kmp.crt.del 2>/dev/null || true)
	for del_cert in $del_certs
	do
		if ! mokutil --delete "$del_cert" --root-pw; then
			echo "Failed to delete $del_cert"
		fi
		rm "$del_cert"
	done
fi
exit 0

%changelog
