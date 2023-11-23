# Spesifikasi API

API akan menyediakan endpoint untuk mengakses data pada setiap tingkat administratif. 
Berikut adalah contoh spesifikasi API sederhana menggunakan style REST:

1. Mendapatkan Semua Provinsi
   - Endpoint: GET /api/provinces
   - Deskripsi: Daftar semua provinsi beserta data geografisnya.
   - Response: </br></br>
      ```json
        {
            "type": "FeatureCollections",
            "features": [
              {
                "type": "Feature",
                "code": "integer",
                "properties" : {
                  "type"  : "string",
                  "code"  : "integer",
                  "name"  : "string",
                  "year"  : "integer|string",
                  "parent": "integer"
                },
                "geometry": {
                  "type": "MultiPolygon",
                  "coordinates" : [
                    [
                      [
                          [
                            91.0000001,
                            1.00000001
                          ],
                          [
                            92.0000002,
                            2.00000002
                          ]
                      ]
                    ]
                  ]
                }
              }
            ]
          }
       ```

2. Mendapatkan Detail Provinsi
      - Endpoint: GET /api/provinces/{provinceId}
      - Deskripsi: Detail dari provinsi tertentu, termasuk daftar kabupaten di dalamnya.
      - Response: <i>sama seperti response endpoint nomor 1</i>

  3. Mendapatkan Semua Kabupaten dalam Provinsi
      - Endpoint: GET /api/provinces/{provinceId}/regencies
      - Deskripsi: Daftar semua kabupaten/kota dalam provinsi tertentu.
      - Response: <i>sama seperti response endpoint nomor 1</i>

 4. Mendapatkan Detail Kabupaten
      - Endpoint: GET /api/regencies/{regencyId}
      - Deskripsi: Detail dari kabupaten tertentu, termasuk daftar distrik di dalamnya.
      - Response: <i>sama seperti response endpoint nomor 1</i>

 5. Mendapatkan Semua Distrik dalam Kabupaten
      - Endpoint: GET /api/regencies/{regencyId}/districts
      - Deskripsi: Daftar semua distrik dalam kabupaten tertentu.
      - Response: <i>sama seperti response endpoint nomor 1</i>


 6. Mendapatkan Detail Distrik
      - Endpoint: GET /api/districts/{districtId}
      - Deskripsi: Detail dari distrik tertentu, termasuk daftar desa di dalamnya.
      - Response: <i>sama seperti response endpoint nomor 1</i>

 7. Mendapatkan Semua Desa dalam Distrik
      - Endpoint: GET /api/districts/{districtId}/villages
      - Deskripsi: Daftar semua Kampung dalam distrik tertentu.
      - Response: <i>sama seperti response endpoint nomor 1</i>

 8. Mendapatkan Detail Kampung
      - Endpoint: GET /api/villages/{villageId}
      - Deskripsi: Detail dari desa tertentu.
      - Response: </br></br>
         ```json
           {
               "type": "FeatureCollections",
               "features": [
                 {
                   "type": "Feature",
                   "code": "integer",
                   "properties" : {
                     "type"  : "string",
                     "code"  : "integer",
                     "name"  : "string",
                     "year"  : "integer|string",
                     "parent": "integer"
                     "households": "integer"
                   },
                   "geometry": {
                     "type": "Polygon",
                     "coordinates" : [
                       [
                         [
                             [
                               91.0000001,
                               1.00000001
                             ],
                             [
                               92.0000002,
                               2.00000002
                             ]
                         ]
                       ]
                     ]
                   }
                 }
               ]
             }
          ```
