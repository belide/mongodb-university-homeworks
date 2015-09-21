use photoshare;

db.albums.ensureIndex({'images': 1});

var cursor = db.images.find();

while(cursor.hasNext()) {
  document = cursor.next();
  var imageId = document._id;

  var albumsCount = db.albums.find({images: imageId}).count();

  if(albumsCount == 0) {
    db.images.remove({_id: imageId});
  }
}

db.images.find({'tags': 'kittens'}).count();
