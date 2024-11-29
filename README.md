# pygeoapi-provider-s3-geojson
An implementation of a GeoJSON provider for Pygeoapi with compatibility for S3 buckets.

## Usage

To use the geojson s3 provider use `S3GeoJSONProvider.S3GeoJSONProvider` in name field of the provider.
```
...
providers:
- type: feature
  name: S3GeoJSONProvider.S3GeoJSONProvider
  data: s3://my-bucket/path/to/file.geojson
  id_field: id
...
```