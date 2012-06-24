Summary:	Simple program for undeleting files from ext3 partition
Summary(pl.UTF-8):   Prosty program do odzyskiwania usuniętych plików na partycjach ext3
Name:		ext3rminator
%define	_pre	pre2
Version:	0.3.0
Release:	0.%{_pre}.1
License:	GPL v2
Group:		Applications/System
Source0:	http://web.glandium.org/debian/repository/experimental/%{name}_0.2.99+%{version}%{_pre}.orig.tar.gz
# Source0-md5:	450ce0405a2be760a1e9ced200c05c72
Patch0:		%{name}-linking.patch
URL:		http://web.glandium.org/debian/repository/experimental/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ext3rminator is a last chance program when you just unthoughtfully
deleted several megabytes of data on an ext3 (or ext2) partition. It
goes through all free blocks in the filesystem to look for what can
look like data.

It is only able to recover files where the 48 first KB (actually, 12
blocks, a block usually being 4096 bytes) are contiguous.

%description -l pl.UTF-8
ext3rminator to program ostatniej szansy w przypadku bezmyślnego
usunięcia wielu megabajtów danych z partycji ext3 (lub ext2).
Przeszukuje wszystkie wolne bloki w systemie plików w poszukiwaniu
czegoś, co wygląda jak dane.

Jest w stanie odzyskać pliki tylko jeśli pierwsze 48 kB (właściwie 12
bloków przy rozmiarze bloku równym zwykle 4096 bajtów) jest ciągłe.

%prep
%setup -q -n %{name}-%{version}%{_pre}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="-I%{_includedir}/et %{rpmcflags}"
export CFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
