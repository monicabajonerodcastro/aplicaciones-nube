# This code is compatible with Terraform 4.25.0 and versions that are backwards compatible to 4.25.0.
# For information about validating this Terraform code, see https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/google-cloud-platform-build#format-and-validate-the-configuration

provider "google" {
  project = "cloud-apps-4204"
  region = "us-west4"
  zone = "us-west4-a"
}

resource "google_compute_instance" "services" {
  boot_disk {
    auto_delete = true
    device_name = "services"

    initialize_params {
      image = "projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20230302"
      size  = 10
      type  = "pd-balanced"
    }

    mode = "READ_WRITE"
  }

  can_ip_forward      = false
  deletion_protection = false
  enable_display      = false

  labels = {
    ec-src = "vm_add-tf"
  }

  machine_type = "f1-micro"

  metadata = {
    startup-script = "#! /bin/bash\n\necho \"********** STARTING SERVICES **********\"\nsudo apt-get update\n\necho \"********** INSTALLING CA-CERTIFICATES / CURL / GNUPG **********\"\nsudo apt-get install -y \\\nca-certificates \\\ncurl \\\ngnupg\n\necho \"********** ADDING THE OFFICIAL GPG KEY **********\"\nsudo install -m 0755 -d /etc/apt/keyrings\n\ncurl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg\n\nsudo chmod a+r /etc/apt/keyrings/docker.gpg\n\necho \"********** SETING UP THE REPOSITORY **********\"\necho \\\n\"deb [arch=\"$(dpkg --print-architecture)\" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \\\n\"$(. /etc/os-release && echo \"$VERSION_CODENAME\")\" stable\" | \\\nsudo tee /etc/apt/sources.list.d/docker.list > /dev/null\n\necho \"********** UPDATING APT-GET **********\"\nsudo apt-get update\n\necho \"********** INSTALLING DOCKER **********\"\nsudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin\n\necho \"********** CREATING THE FILES FOLDER **********\"\nsudo mkdir files\n\necho \"********** CREATING THE VOLUME **********\"\nsudo docker volume create --driver local \\\n      --opt type=none \\\n      --opt device=/files \\\n      --opt o=bind \\\n      files\n\necho \"********** SETTING UP GIT VARIABLES **********\"\ngit config --global user.name \"Monica Bajonero\"\ngit config --global user.email m.bajonero@uniandes.edu.co\n\necho \"********** CLONING THE REPOSITORY **********\"\ngit clone https://github.com/monicabajonerodcastro/aplicaciones-nube.git\n\necho \"********** CD FOLDER **********\"\ncd aplicaciones-nube\n\necho \"********** CHECKOUT TO THE BRANCH **********\"\ngit fetch && git checkout feature/pub-sub-conf\n\necho \"********** PULLING THE LAST CHANGES **********\"\ngit pull origin feature/pub-sub-conf\n\necho \"********** CD FOLDER TO RUN **********\"\ncd services\n\necho \"********** DOCKER COMPOSE UP **********\"\nsudo docker compose up --build -d\n\necho \"********** FINISHED SERVICES **********\"\n\nEOF"
  }

  name = "services"

  network_interface {
    access_config {
      network_tier = "PREMIUM"
    }

    subnetwork = "projects/cloud-apps-4204/regions/us-west4/subnetworks/default"
  }

  scheduling {
    automatic_restart   = true
    on_host_maintenance = "MIGRATE"
    preemptible         = false
    provisioning_model  = "STANDARD"
  }

  service_account {
    email  = "253779523910-compute@developer.gserviceaccount.com"
    scopes = ["https://www.googleapis.com/auth/devstorage.read_only", "https://www.googleapis.com/auth/logging.write", "https://www.googleapis.com/auth/monitoring.write", "https://www.googleapis.com/auth/service.management.readonly", "https://www.googleapis.com/auth/servicecontrol", "https://www.googleapis.com/auth/trace.append"]
  }

  shielded_instance_config {
    enable_integrity_monitoring = true
    enable_secure_boot          = false
    enable_vtpm                 = true
  }

  zone = "us-west4-a"
}
