use enron;

db.messages.find({
    $and: [
        {'headers.From': 'andrew.fastow@enron.com'},
        {'headers.To':
            {$in: [
                'jeff.skilling@enron.com'
            ]}
        }
    ]
}).count();
