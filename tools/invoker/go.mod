module github.com/ease-lab/vSwarm/tools/invoker

go 1.16

replace (
	github.com/ease-lab/vSwarm/tools/benchmarking_eventing => ../benchmarking_eventing
	github.com/ease-lab/vSwarm/tools/endpoint => ../endpoint
	github.com/ease-lab/vSwarm/utils/tracing/go => ../../utils/tracing/go
)

require (
	github.com/containerd/containerd v1.5.8
	github.com/ease-lab/vSwarm/tools/benchmarking_eventing v0.0.0-00010101000000-000000000000
	github.com/ease-lab/vSwarm/tools/endpoint v0.0.0-00010101000000-000000000000
	github.com/ease-lab/vSwarm/utils/tracing/go v0.0.0-00010101000000-000000000000
	github.com/golang/protobuf v1.5.2
	github.com/google/uuid v1.3.0
	github.com/sirupsen/logrus v1.8.1
	go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc v0.20.0
	google.golang.org/grpc v1.46.0
	google.golang.org/protobuf v1.28.0
)
