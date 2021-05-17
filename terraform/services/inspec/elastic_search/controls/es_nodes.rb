content = inspec.profile.file("terraform_output.json")
params = JSON.parse(content)

es_endpoint = params['es_endpoint']['value']
es_user_key = params['access_ids']['value']
es_user_secret = params['secret_keys']['value']

secure_es_endpoint = 'https://' + es_endpoint

control 'es_nodes' do
  title 'ES Nodes must exist and be in a valid state'
  impact 1.0

  describe http('http://' + es_endpoint) do
    its('status') { should cmp 408 }
  end

  describe http('https://' + es_endpoint) do
    its('status') { should cmp 403 }
  end

  describe http('https://' + es_endpoint, enable_remote_worker: true) do
    its('status') { should cmp 403 }
  end

  
  # describe elasticsearch do
  #   # url: es_endpoint
  #   its('version') { should cmp '6.0' }
  # end

  describe elasticsearch(url: secure_es_endpoint, username: es_user_key, password: es_user_secret) do
    # its('version') { should cmp '6.0' }
    it { should exist }
  end

  ##
  # Signing the AWS auth headers would be a bit of a pain, inspec doesn't seem to have mature AWS support
  ##
  # describe http('https://' + es_endpoint,
  #             auth: {user: 'AKIAJISCG53W2SBQGJAA', pass: 'D+d2aAPRfrUqLTlWZAuE/hQqs3JILLIvcnp1xBsA'},
  #             method: 'GET'
  #         ) do
  #   its('status') { should cmp 200 }
  #   its('body') { should cmp 'pong' }
  #   its('headers.Content-Type') { should cmp 'application/json' }
  # end



end

