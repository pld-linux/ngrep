Name:		ngrep
Version:	1.38
BuildRequires:	libpcap-devel
Summary:	A program that mimicks as much functionality in GNU grep as possible, applied at the network layer.
Summary(pl):	Program spe³niaj±cy zadania GNU grep na poziomie sieci.
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://www.packetfactory.net/Projects/ngrep/%{name}-%{version}.tar.gz
URL:		http://www.packetfactory.net/Projects/ngrep
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ngrep strives to provide most of GNU grep's common features, applying
them to the network layer. ngrep is a pcap-aware tool that will allow
you to specify extended regular expressions to match against data
payloads of packets. It currently recognizes TCP and UDP across
ethernet, ppp and slip interfaces, and understands bpf filter logic in
the same fashion as more common packet sniffing tools, like tcpdump
and snoop.

%description -l pl
Ngrep próbuje wype³niæ zadania stawiane grep-owi, w odniesieniu do
poziomu sieci. Ngrep korzysta z biblioteki pcap, pozwala na
korzystanie z wyra¿eñ regularnych zastosowanych do pakietów czy
kawa³ków danych. Obecnie obrabia pakiety TCP i UDP przychodz±ce na
interfejsy ethernet, ppp i slip. Ngrep zna zasady filtrowania bpf w
takim samym stylu jak czê¶ciej u¿ywane pakiety typu tpcdump czy snoop.

%prep
%setup -q -n %{name}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_sbindir}
%{__install} ngrep $RPM_BUILD_ROOT%{_sbindir}
%{__install} -d $RPM_BUILD_ROOT%{_mandir}/man8
%{__install} ngrep.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf BUGS CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%doc *.gz
