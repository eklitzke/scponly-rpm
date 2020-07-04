Name:     scponly
Version:  20110526
Release:  0
Summary:  Restricted shell for ssh and scp only access
Group: 	  System/Shells
License:  GPL
Url: 	    http://www.sublimation.org/scponly/wiki/index.php
Source0:  https://sourceforge.net/projects/scponly/files/scponly-snapshots/scponly-%{version}.tgz
Patch0:   scponly-20110526-Makefile-ownership.patch

BuildRequires: openssh
BuildRequires: rsync
Requires: rsync
Requires: openssh

%description
scponly is an alternative 'shell' (of sorts) for system administrators who would like to provide access
to remote users to both read and write local files without providing any remote execution priviledges.
Functionally, it is best described as a wrapper to the tried and true ssh suite of applications.
A typical usage of scponly is in creating a semi-public account not unlike the concept of anonymous login for ftp.
This allows an administrator to share files in the same way an anon ftp setup would,
only employing all the protection that ssh provides. This is especially significant
if you consider that ftp authentications traverse public networks in a plaintext format.

%prep

%setup -q

chmod a-x CHANGELOG INSTALL TODO CONTRIB README COPYING *.h *.c
%patch0

%build
%configure --with-sftp-server=%{_libexecdir}/ssh/sftp-server --enable-scp-compat --enable-rsync-compat
%make_build

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG INSTALL TODO CONTRIB README COPYING
%dir %_sysconfdir/scponly
%config %attr (644,root,root) %{_sysconfdir}/scponly/debuglevel
%attr (755,root,root) %{_bindir}/scponly
%attr (644,root,root) %{_mandir}/man8/scponly.8.gz
%changelog
