Summary:	Networked grep
Summary(pl.UTF-8):	Sieciowy grep
Name:		ngrep
Version:	1.45
Release:	5
License:	BSD
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/ngrep/%{name}-%{version}.tar.bz2
# Source0-md5:	bc8150331601f3b869549c94866b4f1c
Patch0:		%{name}-cflags.patch
Patch1:		%{name}-pcap.patch
URL:		http://ngrep.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel >= 2:1.0.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ngrep strives to provide most of GNU grep's common features, applying
them to the network layer. ngrep is a pcap-aware tool that will allow
you to specify extended regular expressions to match against data
payloads of packets. It currently recognizes TCP and UDP across
ethernet, ppp and slip interfaces, and understands bpf filter logic in
the same fashion as more common packet sniffing tools, like tcpdump
and snoop.

%description -l pl.UTF-8
Ngrep próbuje wypełnić zadania stawiane grep-owi, w odniesieniu do
poziomu sieci. Ngrep korzysta z biblioteki pcap, pozwala na
korzystanie z wyrażeń regularnych zastosowanych do pakietów czy
kawałków danych. Obecnie obrabia pakiety TCP i UDP przychodzące na
interfejsy ethernet, ppp i slip. Ngrep zna zasady filtrowania bpf w
takim samym stylu jak częściej używane pakiety typu tpcdump czy snoop.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--enable-ipv6 \
	--disable-pcap-restart
%{__make} \
	MAKEFLAGS= \
	STRIPFLAG=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install ngrep $RPM_BUILD_ROOT%{_sbindir}
install ngrep.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt doc/{CHANGES,CREDITS,README,REGEX}.txt
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
