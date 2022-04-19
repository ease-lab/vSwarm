module github.com/ease-lab/vSwarm/tools/relay

go 1.16

replace github.com/ease-lab/vSwarm/utils/tracing/go => ../../utils/tracing/go

require (
	github.com/ease-lab/vSwarm-proto v0.0.0-20220425132824-72aa8060e781
	github.com/ease-lab/vSwarm/utils/tracing/go v0.0.0-20220421212014-f17df208fc40
	github.com/sirupsen/logrus v1.8.1
	google.golang.org/grpc v1.45.0
)

require (
	github.com/containerd/containerd v1.5.10 // indirect
	github.com/go-logr/logr v1.2.3 // indirect
	github.com/go-logr/stdr v1.2.2 // indirect
	github.com/golang/protobuf v1.5.2 // indirect
	github.com/openzipkin/zipkin-go v0.4.0 // indirect
	go.opentelemetry.io/contrib v0.20.0 // indirect
	go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc v0.31.0 // indirect
	go.opentelemetry.io/otel v1.6.3 // indirect
	go.opentelemetry.io/otel/exporters/trace/zipkin v0.20.0 // indirect
	go.opentelemetry.io/otel/exporters/zipkin v1.6.3 // indirect
	go.opentelemetry.io/otel/sdk v1.6.3 // indirect
	go.opentelemetry.io/otel/trace v1.6.3 // indirect
	go.uber.org/goleak v1.1.10 // indirect
	golang.org/x/net v0.0.0-20220412020605-290c469a71a5 // indirect
	golang.org/x/sys v0.0.0-20220412211240-33da011f77ad // indirect
	golang.org/x/text v0.3.7 // indirect
	google.golang.org/genproto v0.0.0-20220414192740-2d67ff6cf2b4 // indirect
	google.golang.org/protobuf v1.28.0 // indirect
)
