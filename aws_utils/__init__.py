def get_bucket_object_key(s3_path):
    splits = s3_path.split("/", 3)  # str.split(separator, maxsplit)
    bucket_name = splits[2]
    object_key = splits[-1]
    return (bucket_name, object_key)


def list_all_objects(s3_client, bucket_name):
    paginator = s3_client.get_paginator("list_objects_v2")
    pages = paginator.paginate(Bucket=bucket_name)

    for page in pages:
        if "Contents" in page:
            for obj in page["Contents"]:
                yield obj


def list_all_objects_with_keywords(s3_client, bucket_name, keywords):
    paginator = s3_client.get_paginator("list_objects_v2")
    pages = paginator.paginate(Bucket=bucket_name)
    results = []
    for page in pages:
        if "Contents" in page:
            for obj in page["Contents"]:
                cur_results = []
                for key in keywords:
                    cur_results.append(obj[key])
                results.append(cur_results)
    return results


def list_all_files(s3_client, bucket_name):
    paginator = s3_client.get_paginator("list_objects_v2")
    pages = paginator.paginate(Bucket=bucket_name)

    for page in pages:
        if "Contents" in page:
            for obj in page["Contents"]:
                yield obj["Key"]


def list_folders(s3_client, bucket_name, prefix):
    response = s3_client.list_objects_v2(
        Bucket=bucket_name, Prefix=prefix, Delimiter="/"
    )

    for prefix_info in response.get("CommonPrefixes", []):
        yield prefix_info["Prefix"]


def list_buckets(s3_client):
    """
    Lists the names of all S3 buckets in the AWS account.
    """
    response = s3_client.list_buckets()

    bucket_names = []
    for bucket in response["Buckets"]:
        bucket_names.append(bucket["Name"])

    return bucket_names
